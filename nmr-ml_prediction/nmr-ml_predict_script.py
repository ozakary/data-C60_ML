import os
import numpy as np
import pandas as pd
import torch
import schnetpack as spk
from ase import Atoms
from ase.db import connect
import schnetpack.atomistic as atm
import schnetpack.representation as rep
from schnetpack.data import Structure
import argparse

# Parse command-line arguments for input/output paths and property
parser = argparse.ArgumentParser(description='Run machine learning model prediction.')
parser.add_argument('--input_path', required=True, help='Path to input CSV file with atomic coordinates')
parser.add_argument('--output_path', required=True, help='Path to save output DB file')
parser.add_argument('--property', required=True, help='Property to predict (e.g., sigma_iso)')
args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path
property = args.property

# Set the device for computation (CUDA if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load the input data with atomic coordinates
try:
    new_molecules = pd.read_csv(input_path)
    print(f"Loaded new molecules data with shape: {new_molecules.shape}")
except FileNotFoundError:
    print(f"Error: {input_path} file not found.")
    exit()

new_molecules = new_molecules.groupby('molecule_name')

# Create a new database for the new dataset
def create_new_db(db_path, molecule_names, molecules):
    with connect(db_path) as db:
        for name in molecule_names:
            mol = molecules.get_group(name)
            atoms = Atoms(symbols=mol.atom.values,
                          positions=[(row.x, row.y, row.z) for row in mol.itertuples()])
            print(f"Writing new molecule '{name}' with {len(atoms)} atoms.")
            db.write(atoms, name=name)

# Create the new DB file for the dataset
new_champs_path = output_path
new_dataset_molecule_names = new_molecules.groups.keys()
create_new_db(db_path=new_champs_path, molecule_names=new_dataset_molecule_names, molecules=new_molecules)

# Load new dataset from the created DB
try:
    new_dataset = spk.data.AtomsData(new_champs_path)
    print(f"Loaded new dataset with size: {len(new_dataset)}")
except Exception as e:
    print(f"Error loading new dataset: {e}")
    exit()

# Define the model structure used for training
class MagneticShielding(atm.Atomwise):
    def __init__(self, property):
        super(MagneticShielding, self).__init__(return_contributions=True)
        self.property = property

    def forward(self, inputs):
        result = super().forward(inputs)
        atom_mask = inputs[Structure.atom_mask].bool()
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

# Function to predict NMR parameters using the pre-trained model
def predict_nmr_parameters(dataset, property):
    model = schnet_model(property)
    try:
        model.load_state_dict(torch.load(f'{property}/output/best_model'))
        print(f"Loaded model for {property}.")
    except FileNotFoundError:
        print(f"Error: Pre-trained model for {property} not found.")
        exit()

    loader = spk.data.AtomsLoader(dataset, batch_size=128, num_workers=2)
    model.eval()

    predictions = []
    with torch.no_grad():
        for batch in loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            result = model(batch)
            predictions += result[property + '_pred'].tolist()

    return predictions

# Function to save the predictions along with original atomic coordinates
def save_predictions(dataset, property):
    predictions = predict_nmr_parameters(dataset, property)

    # Load the original structure file to get molecule_name, atom_index, atom, x, y, z
    original_structure_df = pd.read_csv(input_path)

    # Create a DataFrame with the original data and predictions as the last column
    df_pred = pd.DataFrame({
        "molecule_name": original_structure_df["molecule_name"],
        "atom_index": original_structure_df["atom_index"],
        "atom": original_structure_df["atom"],
        "x": original_structure_df["x"],
        "y": original_structure_df["y"],
        "z": original_structure_df["z"],
        "Prediction": predictions  # Save predictions as the last column
    })

    # Save to a CSV file in the same folder as the output DB
    output_dir = os.path.dirname(output_path)
    output_file = f'{output_dir}/{property}_new_predictions_with_structures.csv'
    
    df_pred.to_csv(output_file, index=False)
    print(f"Saved predictions and structures for {property} to '{output_file}'")

# Predict and save results for the new dataset
save_predictions(new_dataset, property)

