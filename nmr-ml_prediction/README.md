# Prediction of NMR Isotropic Magnetic Shielding from the Trained NMR-ML SchNet Model  
**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
**Personal Website:** [Ouail Zakary - personal webpage](https://ozakary.github.io/)

This repository contains code and workflows for predicting NMR isotropic magnetic shielding for carbon atoms using the pre-trained SchNet model. The workflow is specifically designed to handle Path Integral Molecular Dynamics (PIMD) simulation data with 32 beads (the corresponding data can be found in this [Zenodo repository](https://github.com/ozakary/data-NMR-ML_C60)).

## Overview

The prediction workflow processes PIMD simulation data across 32 beads ([Zenodo repository](https://github.com/ozakary/data-NMR-ML_C60)), splitting large trajectory files into chunks of 1001 structures (the size the model was trained on) and converting them to the appropriate format for prediction with the SchNet model.

## Directory Structure

The workflow creates the following directory structure:

```
./nmr-ml_predict_schnet_carpo2.job            # SLURM job script
./nmr-ml_predict_script.py                    # Main prediction script
./concat_csvs.py                              # Script to concatenate results
./code_seperate.py                            # Script to split trajectory files
./code_convert.py                             # Script to convert XYZ to CSV
./sigma_iso/                                  # Directory containing pre-trained model
    /output/
        /best_model                           # Best model checkpoint
./input/                                      # Input files directory
./0/                                          # Bead 0 directory
    /beads_dump_0.xyz                         # Trajectory file for bead 0 (All '.xyz' for this example can be found at this Zenodo repository: https://github.com/ozakary/data-NMR-ML_C60)
    /code_seperate.py                         # Local copy of splitting script (modified for this bead)
    /predicted_sigma_iso_beads_0.csv          # Final concatenated results for bead 0
    /1/                                       # Chunk 1 directory
        /split_beads_dump_0_1.xyz             # Split trajectory chunk
        /code_convert.py                      # Local copy of conversion script (modified for this chunk)
        /converted_split_beads_dump_0_1.csv   # Converted data for SchNet
        /CHAMPS_new_test.db                   # Database file for SchNet
        /sigma_iso_new_predictions_with_structures.csv # Prediction results
    /2/                                       # Additional chunk directories
        ...
    ...
    /5/
        ...
./1/                                          # Bead 1 directory
    ...
...
./31/                                         # Bead 31 directory
    ...
```

## Workflow Steps

### 1. Create Bead Directories

Create directories for each PIMD bead (0-31):

```bash
for i in $(seq 0 1 31); do 
  mkdir ${i}
done
```

### 2. Copy XYZ Files to Bead Directories

Copy the corresponding trajectory files to each bead directory:

```bash
for i in $(seq 0 1 31); do 
  cp beads_dump_${i}.xyz ${i}/
done
```

### 3. Split Trajectories into 1001-Structure Chunks

Copy, modify, and run the separation script in each bead directory:

```bash
for i in $(seq 0 1 31); do 
  cp code_seperate.py ${i}/
  sed -i "s/dump\_0/dump\_${i}/g" ${i}/code_seperate.py
  cd ${i}
  python3 code_seperate.py
  cd ../
done
```

### 4. Create Chunk Directories

Create directories for each chunk and move the split files:

```bash
for i in $(seq 0 1 31); do 
  for j in $(seq 1 1 5); do 
    mkdir ${i}/${j}
    mv ${i}/split_beads_dump_${i}_${j}.xyz ${i}/${j}/
  done
done
```

This example assumes 5 chunks per bead. Adjust according to your specific dataset.

### 5. Convert XYZ Files to SchNet CSV Format

Copy, modify, and run the conversion script in each chunk directory:

```bash
for i in $(seq 0 1 31); do 
  for j in $(seq 1 1 5); do 
    cp code_convert.py ${i}/${j}
    sed -i "s/dump\_0\_1/dump\_${i}\_${j}/g" ${i}/${j}/code_convert.py
    cd ${i}/${j}
    python3 code_convert.py
    cd ../../
  done
done
```

### 6. Run Prediction Job

Submit the prediction job to the cluster:

```bash
sbatch nmr-ml_predict_schnet_carpo2.job
```

**IMPORTANT**: Before running the job, ensure that the loop indices in the job script match your folder structure (number of beads and chunks).

### 7. Monitor Prediction Progress

Check the prediction status:

```bash
grep "Saved predictions and structures" ml_nmr-output_<JOB_ID>.txt
```

### 8. Concatenate Results

After all predictions are complete, concatenate the CSV files for each bead:

```bash
python3 concat_csvs.py
```

This creates consolidated CSV files for further analysis, with one file per bead:
- `./0/predicted_sigma_iso_beads_0.csv`
- `./1/predicted_sigma_iso_beads_1.csv`
- ...
- `./31/predicted_sigma_iso_beads_31.csv`

## Script Functions

### `code_seperate.py`

This script reads a trajectory XYZ file and splits it into chunks of 1001 structures. It identifies structure boundaries in the XYZ file by looking for the "60" marker (corresponding to the number of atoms in C60) and creates separate files with the specified number of structures.

### `code_convert.py`

This script converts XYZ files to the CSV format required by SchNet. It creates a CSV file with the following columns:
- molecule_name (e.g., "empty_fullerene_100000")
- atom_index (0-59 for each atom in C60)
- atom (always "C" for carbon)
- x, y, z (atomic coordinates)

### `ml-predict.py`

This script loads the pre-trained SchNet model and predicts NMR isotropic shielding values for the provided structures. It:
1. Creates a SchNetPack-compatible database from the CSV file
2. Loads the pre-trained model
3. Makes predictions for each structure
4. Saves the results with the original structural information

### `concat_csvs.py`

This script concatenates the prediction results from each chunk into a single file per bead. It collects all `sigma_iso_new_predictions_with_structures.csv` files from each chunk directory and combines them into a single CSV file in the parent bead directory.

## Job Script Details

The `nmr-ml_predict_schnet_carpo2.job` script:
- Allocates 4 NVIDIA V100 GPUs
- Uses 16 CPU cores (4 tasks × 4 CPUs per task)
- Runs for up to 3 days
- Activates the SchNet virtual environment
- Processes each chunk of each bead sequentially, running the prediction script with appropriate parameters

## Output Files

After running the complete workflow, you will have the following output files:

1. In each bead folder (from 0 to 31):
   - `./0/predicted_sigma_iso_beads_0.csv`
   - `./1/predicted_sigma_iso_beads_1.csv`
   - ...
   - `./31/predicted_sigma_iso_beads_31.csv`

2. In each chunk folder (for all beads and chunks):
   - `./0/1/split_beads_dump_0_1.xyz` (Split trajectory chunk)
   - `./0/1/converted_split_beads_dump_0_1.csv` (Converted data for SchNet)
   - `./0/1/CHAMPS_new_test.db` (Database file for SchNet)
   - `./0/1/sigma_iso_new_predictions_with_structures.csv` (Prediction results)
   - ...
   - `./31/5/sigma_iso_new_predictions_with_structures.csv`

---

For further details, please refer to the respective folders or contact the author via the provided email.
