# C<sub>60</sub> Fullerene Dataset Preparation for Training the MLIP-3 NEP3 Architecture

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---

This document describes the preparation of datasets for training the MLIP-3 NEP3 architecture.

## Directory Contents

The `DFT-3` directory contains the processed data files necessary for training machine learning models to predict energy and forces from molecular structures. The dataset contains C<sub>60</sub> fullerene structures and their corresponding energy and force components acting on each atom calculated using `TURBOMOLE`.

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

### train.xyz
```
60
energy=-28.98359243818 config_type=nep3xyz Lattice="25.0 0.0 0.0 0.0 25.0 0.0 0.0 0.0 25.0" Properties=species:S:1:pos:R:3:force:R:3
C 13.74147384 11.89484967 15.90732695 0.0443671851007901 -1.2721796915656978 -2.380931760731759
C 12.49586283 12.65890140 16.05387593 0.6794097409759259 -1.9876823393016938 0.8233933623596119
...
C 11.61780476 14.30220511 9.71062469 0.7380568373487346 5.512827104222751 1.4773563054087615
60
energy=-28.8439249616 config_type=nep3xyz Lattice="25.0 0.0 0.0 0.0 25.0 0.0 0.0 0.0 25.0" Properties=species:S:1:pos:R:3:force:R:3
C 13.68487194 11.89837020 15.76845340 0.9751354975807374 -2.4910155503456086 -0.5606255108955936
C 12.53116534 12.62739222 16.00473695 -2.1867771652838073 2.740137827912325 0.6819832962717431
...
```

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
- The **train.xyz** and **test.xyz** files for MLIP-3 do not use the additional reference data produced from active learning as MLIP-1 does
- Reference DFT energy from `TURBOMOLE` for each structure in the **train.xyz** and **test.xyz** files has been shifted by +62100 eV

---

For further details, please refer to the respective folders or contact the author via the provided email.

