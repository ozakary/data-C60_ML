import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ase import Atoms
from ase.db import connect
import torch
import torch.nn.functional as F
from torch.optim import Adam
import schnetpack as spk
import schnetpack.atomistic as atm
import schnetpack.representation as rep
from schnetpack.datasets import *
from schnetpack.data import Structure

# Set the device for computation (CUDA if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load and process data
molecules = pd.read_csv('./input/structures.csv')
print(f"Loaded molecules data with shape: {molecules.shape} and columns: {molecules.columns.tolist()}")

molecules = molecules.groupby('molecule_name')
magnetic_shielding_tensors = pd.read_csv('./input/magnetic_shielding_tensors.csv')
print(f"Loaded magnetic shielding tensors with shape: {magnetic_shielding_tensors.shape} and columns: {magnetic_shielding_tensors.columns.tolist()}")

# Process magnetic shielding tensors
x = magnetic_shielding_tensors.columns.values[2:]
x = magnetic_shielding_tensors[x].values
print(f"Raw tensor shape: {x.shape}, type: {type(x)}")

x = x.reshape(-1, 3, 3)
print(f"Reshaped tensor shape: {x.shape}")

x = x + np.transpose(x, (0, 2, 1))
x = 0.5 * x
w, v = np.linalg.eigh(x)
print(f"Eigenvalues shape: {w.shape}")

sigma_iso = np.sum(w, axis=1) / 3
omega = w[:, 2] - w[:, 0]
kappa = 3 * (sigma_iso - w[:, 1]) / omega

print(f"sigma_iso shape: {sigma_iso.shape}, omega shape: {omega.shape}, kappa shape: {kappa.shape}")

# Create DataFrame for magnetic shielding parameters
magnetic_shielding_parameters = magnetic_shielding_tensors[magnetic_shielding_tensors.columns.values[:2]]
magnetic_shielding_parameters = pd.DataFrame(magnetic_shielding_parameters)
magnetic_shielding_parameters["sigma_iso"] = sigma_iso
magnetic_shielding_parameters["omega"] = omega
magnetic_shielding_parameters["kappa"] = kappa

print(f"Magnetic shielding parameters shape: {magnetic_shielding_parameters.shape}")

# Save processed data
magnetic_shielding_parameters.head(10).to_csv('magnetic_shielding_parameters_head.csv', index=False)
print("Saved magnetic shielding parameters head to 'magnetic_shielding_parameters_head.csv'")

# Plot histograms
def plot_histogram(data, column, filename):
    plt.figure()
    data[column].hist(bins=100)
    plt.title(f'Histogram of {column}')
    plt.savefig(filename)
    plt.close()
    print(f"Saved histogram for {column} to '{filename}'")

plot_histogram(magnetic_shielding_parameters, 'sigma_iso', 'sigma_iso_hist.png')
plot_histogram(magnetic_shielding_parameters, 'omega', 'omega_hist.png')
plot_histogram(magnetic_shielding_parameters, 'kappa', 'kappa_hist.png')

# Load training data
train = pd.read_csv('./input/train.csv')
print(f"Loaded training data with shape: {train.shape} and columns: {train.columns.tolist()}")

train_molecule_names = train.molecule_name.unique()
print(f"Unique molecule names in training data: {len(train_molecule_names)}")

msp = magnetic_shielding_parameters.groupby('molecule_name')

# Create database
def create_db(db_path, molecule_names):
    with connect(db_path) as db:
        for name in molecule_names:
            mol = molecules.get_group(name)
            atoms = Atoms(symbols=mol.atom.values,
                          positions=[(row.x, row.y, row.z) for row in mol.itertuples()])
            try:
                mol_msp = msp.get_group(name)
                sigma_iso = mol_msp['sigma_iso'].values.reshape(-1, 1)
                omega = mol_msp['omega'].values.reshape(-1, 1)
                kappa = mol_msp['kappa'].values.reshape(-1, 1)
                print(f"Writing molecule '{name}' with shapes: sigma_iso {sigma_iso.shape}, omega {omega.shape}, kappa {kappa.shape}")
            except KeyError:
                sigma_iso, omega, kappa = [None] * 3
                print(f"Skipping molecule '{name}' due to missing data")
            db.write(atoms, name=name, data=dict(sigma_iso=sigma_iso, omega=omega, kappa=kappa))

champs_path = 'CHAMPS_train.db'
dataset_size = len(train_molecule_names)
dataset_molecule_names = train_molecule_names[:dataset_size]
create_db(db_path=champs_path, molecule_names=dataset_molecule_names)

# Check the number of molecules in the database
with connect(champs_path) as db:
    print(f"Number of molecules in database: {len(db)}")

# Load dataset
dataset = spk.data.AtomsData(champs_path, properties=['sigma_iso', 'omega', 'kappa'])
print(f"Loaded dataset with size: {len(dataset)}")

# Define model components
class MagneticShielding(atm.Atomwise):
    def __init__(self, property):
        super(MagneticShielding, self).__init__(return_contributions=True)
        self.property = property

    def forward(self, inputs):
        result = super().forward(inputs)
        atom_mask = inputs[Structure.atom_mask].bool()
        yi = inputs[self.property]
        yi = torch.masked_select(yi.squeeze(dim=2), atom_mask)
        inputs[self.property + '_true'] = yi
        yi = result['yi']
        yi = torch.masked_select(yi.squeeze(dim=2), atom_mask)
        result[self.property + '_pred'] = yi
        return result

def schnet_model(property):
    reps = rep.SchNet(n_interactions=6)
    output = MagneticShielding(property=property)
    model = atm.AtomisticModel(reps, output)
    model = model.to(device)
    return model

# Define training and evaluation functions
def evaluate_dataset(metrics, model, loader, device):
    for metric in metrics:
        metric.reset()
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            result = model(batch)
            for metric in metrics:
                metric.add_batch(batch, result)
    results = [metric.aggregate() for metric in metrics]
    return results

def train_model(property, max_epochs=100000):
    n_dataset = len(dataset)
    n_val = n_dataset // 10
    train_data, val_data, test_data = dataset.create_splits(n_dataset - n_val * 2, n_val)
    train_loader = spk.data.AtomsLoader(train_data, batch_size=64, num_workers=2)
    val_loader = spk.data.AtomsLoader(val_data, batch_size=128, num_workers=2)

    model = schnet_model(property)
    target_key = property + '_true'
    output_key = property + '_pred'
    opt = Adam(model.parameters(), lr=1e-4)
    loss = lambda b, p: F.mse_loss(p[output_key], b[target_key])
    metrics = [
        spk.metrics.MeanAbsoluteError(target_key, output_key, name='MAE_' + property),
        spk.metrics.RootMeanSquaredError(target_key, output_key, name='RMSE_' + property),
    ]
    hooks = [
        spk.train.MaxEpochHook(max_epochs),
        spk.train.CSVHook(property + '/log', metrics, every_n_epochs=1),
    ]
    trainer = spk.train.Trainer(property + '/output', model, loss, opt, train_loader, val_loader, hooks=hooks)
    
    print(f"Starting training for property: {property}")
    trainer.train(device)

    model.load_state_dict(torch.load(property + '/output/best_model'))
    test_loader = spk.data.AtomsLoader(test_data, batch_size=128, num_workers=2)
    model.eval()

    df = pd.DataFrame()
    df['metric'] = ['MAE', 'RMSE']
    df['training'] = evaluate_dataset(metrics, model, train_loader, device)
    df['validation'] = evaluate_dataset(metrics, model, val_loader, device)
    df['test'] = evaluate_dataset(metrics, model, test_loader, device)
    df.to_csv(f'{property}_evaluation_metrics.csv', index=False)

    return test_data

def show_history(property):
    df = pd.read_csv(property + '/log/log.csv')
    df.tail().to_csv(f'{property}_training_history_tail.csv', index=False)
    max_value = df[['MAE_' + property, 'RMSE_' + property]].max().max() * 1.1
    df[['MAE_' + property, 'RMSE_' + property]].plot(ylim=(0, max_value))
    plt.title(f'Training History for {property}')
    plt.savefig(f'{property}_training_history.png')
    plt.close()
    print(f"Saved training history for {property} to '{property}_training_history.png'")

def test_prediction(dataset, property):
    model = schnet_model(property)
    model.load_state_dict(torch.load(property + '/output/best_model'))
    loader = spk.data.AtomsLoader(dataset, batch_size=128, num_workers=2)
    model.eval()

    targets = []
    predictions = []
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            result = model(batch)
            targets += batch[property + '_true'].tolist()
            predictions += result[property + '_pred'].tolist()
    return targets, predictions

def show_predictions(dataset, property):
    targets, predictions = test_prediction(dataset, property)
    df_pred = pd.DataFrame()
    df_pred['Target'] = targets
    df_pred['Prediction'] = predictions
    df_pred.plot.scatter(x='Target', y='Prediction', title=property)
    plt.savefig(f'{property}_predictions.png')
    plt.close()

used_test_data = dict()
for p in ['sigma_iso', 'omega', 'kappa']:
    print(p)
    used_test_data[p] = train_model(p, max_epochs=5000)
    show_history(p)

for p in ['sigma_iso', 'omega', 'kappa']:
    show_predictions(used_test_data[p], p)

