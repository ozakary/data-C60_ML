# C<sub>60</sub> Fullerene DFT Calculations

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

This repository contains the calculation conditions used in the DFT reference data computations for the NEP machine learning interatomic potentials of C<sub>60</sub> fullerene system described in the manuscript “***Neural Networks-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene***”. [DOI: TBA]

## Overview of the Data

This project contains computational data for C<sub>60</sub> structures. Each structure was computed using the computational conditions described in the sections below.  

The reference DFT values are calculated for all empty C<sub>60</sub> structures in the reference dataset at three levels of DFT theory, which we refer to as DFT-1, DFT-2, and DFT-3.

Here we provide one example calculation folder `cluster_<ID>` for each DFT theory level used (DFT-1, DFT-2, and DFT-3). These example Turbomole DFT calculation data files can be found in the corresponding subdirectories.

Directory structure example:
```
./cluster_<ID>/
    energy
    gradient
    mpshift.out
    rdgrad.out
    ridft.out
    statistics
    ref.xyz
    auxbasis
    basis
    control
    coord
    coord_34500.xyz
    createxyz.py
    merge.py
    turbomole_carpo2.job OR tm77_puhti.job

```
To start the calculation and process the results, all the necessary Turbomole input files should be included in the desired directory. The calculation produces the following output files:
    `energy`, 
    `gradient`, 
    `mpshift.out`, 
    `rdgrad.out`, 
    `ridft.out`, and 
    `statistics`.
    

Each `cluster_<ID>` folder also contains the corresponding `.job` file (`tm77_puhti.job` or `turbomole_carpo2.job`) as well as the job log files:
- Output log: `jobfile.out<JOB_ID>`
- Error log: `jobfile.err<JOB_ID>`

## Computational Details

### General Settings
- **Program Package**: `TURBOMOLE rev. V7-7`
- **System**: C<sub>60</sub> fullerene
- **Calculation Type**: DFT optimization with NMR shielding parameters

### DFT Methods
- **Functional**: `PBE0` hybrid functional with `25%` exact exchange
- **Basis Set**:  
- `DFT-1` and `DFT-2` : `x2c-TZVPall-s` (relativistically recontracted triple-zeta valence basis set with polarization functions)
  - (`11s7p2d1f`) primitive Gaussian functions contracted to `[5s4p2d1f]`
- `DFT-3` : `pcSseg-1` (segmented contracted basis set, optimized for calculating nuclear magnetic shielding constants)
- **Auxiliary Basis Set**:  
- `DFT-1` and `DFT-2` : `x2c-TZVPall-s` (`12s5p4d2f1g`)
- `DFT-3` : `pcSseg-1` (`12s5p4d2f1g`)
- **Relativistic Treatment**: Diagonal Local Approximation (`DLU`) with Exact Two-Component (`X2C`) Hamiltonian
- **Dispersion Correction**:  
- `DFT-1` : `DFT-D4` dispersion model
- `DFT-2` and `DFT-3:` no dispersion model used

### SCF Parameters
- **Convergence Criterion**: 10<sup>-7</sup> (DFT-1) or 10<sup>-8</sup> (DFT-2 and DFT-3) atomic units
- **Maximum Iterations**: 100
- **Convergence Acceleration**:
  - Damping (start=3.300, step=0.050, min=0.100)
  - Direct Inversion in the Iterative Subspace (`DIIS`)

### NMR Calculations
- **Method**: `MPSHIFT` module with gauge-including atomic orbital (`GIAO`) approach
- **Functional**: `PBE0` (same as optimization)
- **Grid Size**: 
  - "4a" for geometry optimization
  - "m3" for NMR-related calculations

### System Properties
- **Number of Atoms**: 60
- **Basis Functions**: 
  - 2340 contracted atomic orbitals (CAO)
  - 2040 atomic orbitals (AO)
- **Occupied Orbitals**: 180 (closed-shell configuration)

## Requirements to Reproduce This Data
- **Package**: [TURBOMOLE rev. V7-7](https://www.turbomole.org/)
- **Input files**:
  - [basis](./DFT-1/input_files/basis): Basis set definition
  - [control](./DFT-1/input_files/control): Main input control file
  - [coord](./DFT-1/input_files/coord): Cartesian coordinates file
  - [coord_ID.xyz](./DFT-1/input_files/coord_34500.xyz): Coordinate file in xyz format
  - [auxbasis](./DFT-1/input_files/auxbasis): Auxiliary basis set for RI approximation
  - [mos](./DFT-1/input_files/mos): Turbomole input file containing the molecular orbitals
- **Additional scripts**:
  - [tm77_puhti.job](./DFT-2/input_files/tm77_puhti.job): Script to call Turbomole DFT calculation in supercomputer Puhti (https://www.puhti.csc.fi/public/)
  - [turbomole_carpo2.job](./DFT-1/input_files/turbomole_carpo2.job): Script to call Turbomole DFT calculation in supercomputer Carpo2
  - [createxyz.py](./DFT-1/input_files/createxyz.py): Produces an xyz-file (ref.xyz) with one C<sub>60</sub> structure containing reference DFT values (called after Turbomole DFT calculations are finished)
  - [merge.py](./DFT-1/input_files/merge.py): Assigns the reference C<sub>60</sub> structure (ref.xyz) to train or test dataset
 
### Workflow of DFT calculations

1. With the input files specified above, produce the initial molecular orbitals by running the Turbomole command `define` and selecting the option `eht`
2. Call the job script to start the calculation

---

- **Computational Resource**: [CSC](https://csc.fi/) Supercomputers [PUHTI](https://www.puhti.csc.fi/public/) and [MAHTI](https://www.mahti.csc.fi/public/)

For further details, please refer to the respective folders or contact the author via the provided email.
