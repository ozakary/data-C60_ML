# C<sub>60</sub> Fullerene DFT and NMR magnetic Shielding Tensor Calculations
**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
**Personal Website:** [Ouail Zakary - personal webpage](https://ozakary.github.io/)

This repository contains the calculation conditions used in the DFT and NMR magnetic shielding tensor computations for the C<sub>60</sub> fullerene system described in the manuscript “***Neural Networks-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene***”. [DOI: TBA]

## Overview of the Data

This project contains computational data for a total of 1001 C<sub>60</sub> structures. Each structure was computed using the computational conditions described in the sections below. The complete input and output files are available in the external `Zenodo` [repository](https://github.com/ozakary/data-NMR-ML_C60).

In the `Zenodo` [repository](https://github.com/ozakary/data-NMR-ML_C60), the Turbomole input and output files for each structure are organized under folders named `cluster_<ID>`, where ID ranges from `0` to `1000`.

Directory structure example:
```
./cluster_0/basis
./cluster_0/control
./cluster_0/coord
./cluster_0/auxbasis
./cluster_0/mpshift.out
./cluster_0/rdgrad.out
./cluster_0/ridft.out
./cluster_1/basis
./cluster_1/control
./cluster_1/coord
./cluster_1/auxbasis
./cluster_1/mpshift.out
./cluster_1/rdgrad.out
./cluster_1/ridft.out
...
...
./cluster_1000/basis
./cluster_1000/control
./cluster_1000/coord
./cluster_1000/auxbasis
./cluster_1000/mpshift.out
./cluster_1000/rdgrad.out
./cluster_1000/ridft.out
```

Each `cluster_<ID>` folder also contains the corresponding `.job` file (`tm77_puhti.job`) as well as the job log files:
- Output log: `jobfile.out<JOB_ID>`
- Error log: `jobfile.err<JOB_ID>`

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
- **Relativistic Treatment**: Exact two-component (`X2C`) Hamiltonian
- **Dispersion Correction**: `DFT-D4` dispersion model

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
  - [auxbasis](./input_files/auxbasis): Auxiliary basis set for RI approximation
  - **Computational Resource**: [CSC](https://csc.fi/) Supercomputers [PUHTI](https://www.puhti.csc.fi/public/) and [MAHTI](https://www.mahti.csc.fi/public/)


---

For further details, please refer to the respective folders or contact the author via the provided email.
