# C<sub>60</sub> Fullerene Dataset Preparation for Training the MLIP-1 NEP3 Architecture

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---

This document describes the preparation of datasets for training the MLIP-1 NEP3 architecture.

## Directory Contents

The `DFT-1` directory contains the processed data files necessary for training machine learning models to predict energy and forces from molecular structures. The dataset contains C<sub>60</sub> fullerene structures and their corresponding energy and force components (as well as magnetic shielding tensor, which will be ignored for now) acting on each atom calculated using `TURBOMOLE`.

## Dataset Files

The dataset consists of two xyz files:

1. **train.xyz**: Contains structural information for all structures assigned to training dataset
2. **test.xyz**: Contains structural information for all structures assigned to test dataset

Both files have the same, standard xyz file structure
   - `energy` : Gives the target energy of the structure in units of eV
   - `config_type`: An optional keyword for labeling that has no effect on the training process
   - `Lattice`: Gives the cell vectors  
     **a** = a<sub>x</sub>**e**<sub>x</sub> + a<sub>y</sub>**e**<sub>y</sub> + a<sub>z</sub>**e**<sub>z</sub>  
     **b** = b<sub>x</sub>**e**<sub>x</sub> + b<sub>y</sub>**e**<sub>y</sub> + b<sub>z</sub>**e**<sub>z</sub>  
     **c** = c<sub>x</sub>**e**<sub>x</sub> + c<sub>y</sub>**e**<sub>y</sub> + c<sub>z</sub>**e**<sub>z</sub>  
   - `Properties`: Provide the structural properties in the form of `properties=property_name:data_type:number_of_columns`  
     but only the following items are read
     - `species:S:1` chemical symbol of the element
     - `pos:R:3` position vector of an atom
     - `force:R:3` target (DFT) force vector acting on an atom

## File Structure Example

An example of dataset file **train.xyz** structure:
```
60
energy=-87.60003760837 config_type=nep3xyz Lattice="25.0 0.0 0.0 0.0 25.0 0.0 0.0 0.0 25.0" Properties=species:S:1:pos:R:3:force:R:3
C 12.76239834 12.03979543 15.99216898 -0.5880535239431679 1.4256071616156805 0.3194747514797377
C 14.08028503 12.05841135 15.52497564 3.424841307281792 -1.140783889219895 1.016676381685736
...
C 12.68116454 11.59181124 9.01495137 1.6049380764691348 -2.120026906057437 1.5959693111895283
60
energy=-87.31051611906 config_type=nep3xyz Lattice="25.0 0.0 0.0 0.0 25.0 0.0 0.0 0.0 25.0" Properties=species:S:1:pos:R:3:force:R:3
C 12.78927368 12.12731931 15.92290154 -2.520181816176924 0.6058518576918551 1.825274041053007
C 14.13605137 11.99494343 15.59973828 1.696422175711945 -0.7179688933868583 -1.0309134827151731
...
```
- The **test.xyz** file has similar structure

## Dataset Preparation

The datasets **train.xyz** and **test.xyz** were prepared using Python scripts (`createxyz.py` and `merge.py`) that process the output files from TURBOMOLE calculations.  

The script `createxyz.py`:

1. Extracts atomic coordinates from `coord_<ID>.xyz` file
2. Reads DFT energy and forces from TURBOMOLE output files `energy` and `gradient`
3. Creates xyz file (`ref.xyz`) of the structure with DFT target energy and forces

The script `merge.py`:

1. Assigns reference structure (`ref.xyz`) into training (70%) and test (30%) set with the given probability

### Running the Script

To generate the dataset, run the Python scripts independently in all directories (`cluster_<ID>`) each containing a single C<sub>60</sub> reference structure:

```bash
python3 createxyz.py
python3 merge.py
```

This can be automated to go through all directories `cluster_<ID>` with a simple shell script 

## Notes

- The dataset is suitable for training NEP or similar neural network architectures for predicting molecular energy and forces
- The datasets `train.xyz` and `test.xyz` contain **additional reference data** structures from **active learning** process (data in [Zenodo repository](https://github.com/ozakary/)), for which the DFT calculations and dataset preparation are performed in similar manner as described above
- Reference DFT energy from `TURBOMOLE` for each structure in the **train.xyz** and **test.xyz** files has been shifted by +62100 eV

---

For further details, please refer to the respective folders or contact the author via the provided email.
