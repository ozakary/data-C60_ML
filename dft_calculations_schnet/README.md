# C<sub>60</sub> Fullerene DFT and NMR Magnetic Shielding Tensor Calculations

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

This repository contains the calculation conditions used in the DFT and NMR magnetic shielding tensor computations for the C<sub>60</sub> fullerene system described in the manuscript “***Neural Networks-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene***”.

[![DOI](https://img.shields.io/badge/DOI-10.26434%2Fchemrxiv--2025--68g6s-yellow.svg)](https://doi.org/10.26434/chemrxiv-2025-68g6s-v2)

## Overview of the Data

This project contains computational data for a total of 1001 C<sub>60</sub> structures. Each structure was computed using the computational conditions described in the sections below. Each of the DFT calculations of the 1001 structures were carried out as described in this page.

Here we provide the input files for one Turbomole DFT calculation used in the NMR magnetic shielding dataset. The output files and the calculation results of the example calculation provided here follow the same structure as the DFT calculations used for the NEP MLIP training, as described [here](../dft_calculations_nep/). The reference NMR magnetic shielding values are collected in the reference/training data file found in this [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0).

Directory structure example:
```
./cluster_<ID>/
    auxbasis
    basis
    control
    coord
    coord_50000.xyz
    energy
    gradient
    mos
    mpshift.out
    rdgrad.out
    ridft.out
    statistics
    turbomole_carpo2.job OR tm77_puhti.job
```
To start the calculation and process the results, all the necessary Turbomole input files should be included in the desired directory.  

Each calculation produces output files, as described [here](../dft_calculations_nep/) in more detail.

The results are collected, and the processed data files used for the training of the SchNet model can be found in this [Fairdata repository](https://doi.org/10.23729/fd-c64c043e-473e-371d-9586-8fd3d04e2fb0).

Details of generating the NMR magnetic shielding training dataset can be found [here](../nmr-ml_dataset/).

## Computational Details

### General Settings
- **Program Package**: `TURBOMOLE rev. V7-7`
- **System**: C<sub>60</sub> fullerene
- **Calculation Type**: DFT optimization with NMR shielding parameters

### DFT Methods
- **Functional**: `PBE0` hybrid functional with `25%` exact exchange
- **Basis Set**: `x2c-TZVPall-s` (relativistically recontracted triple-zeta valence basis set with polarization functions)
  - (`11s7p2d1f`) primitive Gaussian functions contracted to `[5s4p2d1f]`
- **Auxiliary Basis Set**: `x2c-TZVPall-s` (`12s5p4d2f1g`)
- **Relativistic Treatment**: Diagonal Local Approximation (`DLU`) with Exact Two-Component (`X2C`) Hamiltonian
- **Dispersion Correction**: `D4` dispersion correction

### SCF Parameters
- **Convergence Criterion**: 10<sup>-8</sup> atomic units
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
  - [basis](./input_files/basis): Basis set definition
  - [control](./input_files/control): Main input control file
  - [coord](./input_files/coord): Cartesian coordinates file
  - [coord_ID.xyz](./input_files/coord.xyz): Coordinate file in xyz format
  - [auxbasis](./input_files/auxbasis): Auxiliary basis set for RI approximation
  - mos: Turbomole input file containing the molecular orbitals.
- **Computational Resource**: [CSC](https://csc.fi/) Supercomputers [PUHTI](https://www.puhti.csc.fi/public/) and [MAHTI](https://www.mahti.csc.fi/public/)
- The Turbomole calculations can be started in Puhti with the job script found [here](../dft_calculations_nep/DFT-2/cluster_50000/tm77_puhti.job)


---

For further details, please refer to the respective folders or contact the author via the provided email.
