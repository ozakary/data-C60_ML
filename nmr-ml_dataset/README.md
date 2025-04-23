# C<sub>60</sub> Fullerene Dataset Preparation for Training the NMR-ML SchNet Architecture
**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
**Personal Website:** [Ouail Zakary - personal webpage](https://ozakary.github.io/)

This document describes the preparation of datasets for training the NMR-ML SchNet architecture.

## Directory Contents

The `nmr-ml_dataset` directory contains the processed data files necessary for training machine learning models to predict NMR shielding parameters from molecular structures. The dataset is focused on C<sub>60</sub> fullerene structures and their corresponding magnetic shielding tensors calculated using `TURBOMOLE`.

## Dataset Files

The dataset consists of three primary CSV files:

1. **structures.csv**: Contains structural information for all structures
   - `molecule_name`: Unique identifier for each structure (format: empty_fullerene_XXXXX)
   - `atom_index`: Index of atom within the structure (0-59 for C<sub>60</sub>)
   - `atom`: Element type (C for carbon in this dataset)
   - `x`, `y`, `z`: Cartesian coordinates in Å

2. **magnetic_shielding_tensors.csv**: Contains the magnetic shielding tensor components for each atom in each structure
   - `molecule_name`: Corresponds to structure identifier
   - `atom_index`: Index of atom within the structure
   - Components of the shielding tensor: `XX`, `YX`, `ZX`, `XY`, `YY`, `ZY`, `XZ`, `YZ`, `ZZ`

3. **train.csv**: Maps the IDs and molecule names for the training set
   - `id`: Sequential identifier
   - `molecule_name`: Corresponds to structure identifier

## File Structure Examples

### structures.csv
```
molecule_name,atom_index,atom,x,y,z
empty_fullerene_100000,0,C,11.11080728,14.69894953,14.86774265
empty_fullerene_100000,1,C,12.1665084,14.04766639,15.69816333
...
empty_fullerene_100000,59,C,13.31739702,9.38060478,10.94272554
empty_fullerene_100400,0,C,10.70302182,14.45185497,14.87378547
...
```

### magnetic_shielding_tensors.csv
```
molecule_name,atom_index,XX,YX,ZX,XY,YY,ZY,XZ,YZ,ZZ
empty_fullerene_100000,0,12.21886648,-7.65880467,-10.81656042,-33.46727985,48.64368939,87.53764536,-71.07825354,53.35758298,55.38394095
empty_fullerene_100000,1,-22.42631433,-10.45497931,-21.0267305,15.78820649,35.9747497,111.13337715,-39.64177246,40.15082594,98.11970453
...
empty_fullerene_100000,59,-13.43578142,-28.94805401,-4.56075781,-49.29027494,80.83963982,43.45292881,-20.64321771,104.4122455,53.93893217
empty_fullerene_100400,0,22.18956521,-16.25801661,-16.17732638,-54.66527071,55.64841647,103.30336043,-59.92123353,63.16414226,43.21928522
...
```

### train.csv
```
id,molecule_name
0,empty_fullerene_100000
1,empty_fullerene_100000
...
59,empty_fullerene_100000
60,empty_fullerene_100400
...
```

## Dataset Preparation

The dataset was prepared using a Python script (`ml_nmr_schnet_dataset_oz-t.py`) that processes the output files from TURBOMOLE calculations. The script:

1. Extracts magnetic shielding tensors from `mpshift.out` files
2. Extracts atomic coordinates from `coord_<ID>.xyz` files 
3. Creates individual CSV files for each structure's tensors and coordinates
4. Concatenates all data into the final dataset files: `structures.csv`, `magnetic_shielding_tensors.csv`, and `train.csv`

The script processes 1001 C60 structures, with each structure containing 60 carbon atoms, resulting in a dataset with 60,060 atomic entries.

### Running the Script

To generate the dataset, run the Python script from the parent directory containing all cluster folders:

```bash
python3 ml_nmr_schnet_dataset_oz-t.py
```

### Directory Structure

**Input Structure (the data can be found in this [Zenodo repository](https://github.com/ozakary/data-NMR-ML_C60)):**
```
./ml_nmr_schnet_dataset_oz-t.py
./cluster_1/
    mpshift.out
    coord_1.xyz
    ...
./cluster_2/
    mpshift.out
    coord_2.xyz
    ...
...
./cluster_1000/
    mpshift.out
    coord_1000.xyz
    ...
```

**Output Structure:**
```
./dataset_schnet_atomic_coordinates/
    empty_fullerene_1.csv
    empty_fullerene_2.csv
    ...
    structures.csv
./dataset_schnet_shielding_tensors/
    empty_fullerene_1.csv
    empty_fullerene_2.csv
    ...
    magnetic_shielding_tensors.csv
./train.csv
```
## Notes

- Each molecule is represented by a unique identifier in the format `empty_fullerene_<ID>`
- The atom indices range from 0 to 59 within each structure
- The magnetic shielding tensor is represented by its 9 components
- The dataset is suitable for training SchNet or similar graph neural network architectures for predicting NMR parameters

---

For further details, please refer to the respective folders or contact the author via the provided email.
