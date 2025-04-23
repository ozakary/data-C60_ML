# NMR-ML SchNet Architecture Training, Validation, and Testing
**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
**Personal Website:** [Ouail Zakary - personal webpage](https://ozakary.github.io/)

This repository contains the code and workflows for training a machine learning model to predict NMR magnetic shielding tensors using the SchNet neural network architecture. The model is trained on a dataset of 1001 C<sub>60</sub> fullerene structures and their corresponding magnetic shielding tensors calculated using TURBOMOLE.

## Installation

The model training uses SchNetPack 0.2.1 with specific version requirements for dependencies. The installation was performed on [CSC](https://csc.fi/) supercomputers ([PUHTI](https://www.puhti.csc.fi/public/), [MAHTI](https://www.mahti.csc.fi/public/)) and the University of Oulu supercomputer [CARPO2](https://ict.oulu.fi/17120/?lang=en), using the following procedure:

```bash
# Load PyTorch version 1.11
module load pytorch/1.11

# Create a directory for SchNet (in scratch directory, not in projappl)
mkdir schnet
cd schnet

# Create a Python virtual environment
python3 -m venv schnet-venv

# Activate the virtual environment
source schnet-venv/bin/activate

# Upgrade pip and Pillow
python -m pip install --upgrade pip
python -m pip install --upgrade pillow

# Install the required packages for SchNetPack
pip install ase==3.17.0 pandas==1.1.5 numpy==1.19.5 schnetpack==0.2.1
```

## Directory Structure

### Input Files
```
./input/
    structures.csv             # Atomic coordinates (cartesian) for all structures
    magnetic_shielding_tensors.csv  # Raw tensor components
    train.csv                  # Mapping of molecule IDs
```

### Script Files
```
./nmr-ml_train-valid-test_script.py                 # Main Python script for model training
./nmr-ml_schnet_carpo2.job                # SLURM job submission script
```

### Output Files
```
# Histograms of magnetic shielding input data
./sigma_iso_hist.png
./omega_hist.png
./kappa_hist.png

# Prediction visualizations (correlation DFT vs NMR-ML)
./sigma_iso_predictions.png
./omega_predictions.png
./kappa_predictions.png

# Training history plots (Err. vs. epochs)
./sigma_iso_training_history.png
./omega_training_history.png
./kappa_training_history.png

# Evaluation metrics (final values of RMSE and MAE for training, validation, and testing)
./sigma_iso_evaluation_metrics.csv
./omega_evaluation_metrics.csv
./kappa_evaluation_metrics.csv

# Training history logs (to plot Err. vs epochs)
./sigma_iso_training_history_tail.csv
./omega_training_history_tail.csv
./kappa_training_history_tail.csv

# Database file
./CHAMPS_train.db

# Model directories for each parameter
./sigma_iso/
    output/
        best_model
        checkpoints/
            checkpoint-5000.pth.tar
            checkpoint-4990.pth.tar
            checkpoint-4980.pth.tar
            ...
    log/
        log.csv
```

## Workflow Description

### Data Preprocessing

The workflow starts by loading the structural data and magnetic shielding tensor components. The script performs the following preprocessing steps:

1. Loads molecular structures and magnetic shielding tensors from CSV files
2. Reshapes the tensor components into 3×3 matrices
3. Symmetrizes the tensors: `Xsym = 0.5 * (X + X.T)`
4. Computes eigenvalues and eigenvectors of each tensor
5. Calculates three scalar NMR parameters:
   - **sigma_iso** (isotropic shielding): Average of the eigenvalues
   - **omega** (span): Difference between largest and smallest eigenvalues
   - **kappa** (skew): Normalized asymmetry parameter

The script produces histograms of these parameters to visualize their distributions.

### Database Creation

The processed data is stored in an ASE database (Atomic Simulation Environment), which is used by SchNetPack for efficient data loading:

1. Creates an ASE database with molecular structures
2. For each molecule, stores:
   - Atomic positions
   - Element types
   - Calculated NMR parameters (sigma_iso, omega, kappa)

### Model Architecture

The SchNet model consists of:

1. **SchNet Representation Layer**: Learns atomic representations through continuous-filter convolutions
   - Features 6 interaction blocks for message passing between atoms
   - Uses continuous-filter convolutions with radial basis functions
   - Employs a cutoff radius to define local chemical environments
   - Handles variable molecular sizes and preserves rotational and translational invariance
   
2. **Atomwise Output Layer**: Predicts per-atom properties
   - Modified to handle the specific NMR parameters (sigma_iso, omega, kappa)
   - Returns both atom-wise contributions and molecular properties
   - Features a custom forward pass to handle tensor properties
   
#### Detailed Network Architecture

The SchNet architecture has the following components:

- **Embedding Layer**: Converts atomic numbers to feature vectors
  - Embeds each atom type into a 128-dimensional feature space

- **Interaction Blocks (6 layers)**: 
  - Each block processes information from neighboring atoms via filter-generating networks
  - Filter-generating networks:
    - 128 radial basis functions (RBFs) for distance expansion
    - 3 dense layers with filter size 128
    - Shifted softplus activation functions

- **Atom-wise Dense Layers**:
  - First layer: 128 → 128 nodes, shifted softplus activation
  - Output layer: 128 → 1 node, linear activation (per property)

- **Readout Function**: Aggregates atomic contributions
  - Sum pooling over all atoms to obtain molecular properties
  - Individual atomic contributions are preserved for atom-wise analysis

- **Total Parameters**: Approximately 300,000 trainable parameters per model

**MagneticShielding Class Implementation**:

The model uses a custom `MagneticShielding` class, which inherits from `atm.Atomwise` in SchNetPack:
```python
class MagneticShielding(atm.Atomwise):
    def __init__(self, property):
        super(MagneticShielding, self).__init__(return_contributions=True)
        self.property = property

    def forward(self, inputs):
        # Custom forward pass that handles both prediction and ground truth
        result = super().forward(inputs)
        atom_mask = inputs[Structure.atom_mask].bool()
        yi = inputs[self.property]
        yi = torch.masked_select(yi.squeeze(dim=2), atom_mask)
        inputs[self.property + '_true'] = yi
        yi = result['yi']
        yi = torch.masked_select(yi.squeeze(dim=2), atom_mask)
        result[self.property + '_pred'] = yi
        return result
```

This custom implementation allows the model to handle atom-specific tensor properties and properly mask atoms during training and prediction.

### Training Process

For each of the three NMR parameters (sigma_iso, omega, kappa), a separate model is trained:

1. Data is split into training (80%), validation (10%), and test (10%) sets
2. Models are trained using:
   - Adam optimizer with learning rate 1e-4
   - Mean squared error (MSE) loss function
   - Batch size of 64 for training and 128 for validation/testing
   - Maximum of 5000 epochs with early stopping

3. Training is monitored with:
   - Mean Absolute Error (MAE)
   - Root Mean Square Error (RMSE)
   - CSV logging of metrics every epoch
   
4. The best model (based on validation loss) is saved for each parameter

### Evaluation and Visualization

After training, the models are evaluated:

1. Performance metrics (MAE and RMSE) are calculated for:
   - Training set
   - Validation set
   - Test set
   
2. Visualization of:
   - Training history (loss curves)
   - Scatter plots of predicted vs. target values

## Execution

To run the training process:

1. Ensure all input files are placed in the `./input/` directory
2. Submit the job to the cluster using:
   ```bash
   sbatch nmr-ml_schnet_carpo2.job
   ```

The job script allocates:
- 4 GPU nodes (NVIDIA V100)
- 16 CPU cores (4 tasks × 4 CPUs per task)
- 72-hour (3-day) runtime

## Model Performance

The final model performance is recorded in the evaluation metrics CSV files for each parameter:

- `sigma_iso_evaluation_metrics.csv`
- `omega_evaluation_metrics.csv`
- `kappa_evaluation_metrics.csv`

Each file contains MAE and RMSE values for training, validation, and test sets.

## Training History

The training history for each parameter is logged in:

```
./sigma_iso/log/log.csv
./omega/log/log.csv
./kappa/log/log.csv
```

Each log file contains columns for:
- Time
- Learning rate
- Training loss
- Validation loss
- MAE
- RMSE

Example log format:
```
Time,Learning rate,Train loss,Validation loss,MAE_sigma_iso,RMSE_sigma_iso
3.4710941314697266,0.0001,7188.150451660156,192.9999542236328,11.730944010416666,13.892442489833575
6.694938659667969,0.0001,1400.2655563354492,77.70671844482422,7.107393229166667,8.8151414480994
...
```

## Visualization

The training process generates several visualization files:

1. Parameter distributions:
   - `sigma_iso_hist.png`
   - `omega_hist.png`
   - `kappa_hist.png`

2. Training histories:
   - `sigma_iso_training_history.png`
   - `omega_training_history.png`
   - `kappa_training_history.png`

3. Prediction quality:
   - `sigma_iso_predictions.png`
   - `omega_predictions.png`
   - `kappa_predictions.png`

These plots help assess model performance and identify potential issues in the training process.

---

For further details, please refer to the respective folders or contact the author via the provided email.
