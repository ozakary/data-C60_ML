# Supporting Data for “Thermal Expansion and Isotope Effects of Chemical Shift of C60-Fullerene Using Machine Learning-Assisted Path Integral Molecular Dynamics”

## Graphical Abstract

![Graphical Abstract](./blank.png)

**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail Zakary - webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
**Personal Website:** [Ouail Zakary - personal webpage](https://ozakary.github.io/)

This repository contains the calculation conditions used in the DFT and NMR magnetic shielding tensor computations for the C<sub>60</sub> fullerene system described in the manuscript “Thermal Expansion and Isotope Effects of Chemical Shift of C60-Fullerene Using Machine Learning-Assisted Path Integral Molecular Dynamics”. [DOI: TBA]

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


## Citations

If you use this data, please cite the following: \
\
**Paper:** Laurila O.; Jacklin T.; Zakary, O.; Lantto P. Thermal Expansion and Isotope Effects of Chemical Shift of C60-Fullerene Using Machine Learning-Assisted Path Integral Molecular Dynamics. *In preparation* **2025**. [DOI: TBA]

\
**Dataset:** Laurila O.; Jacklin T.; Zakary, O.; Lantto P. (**2025**). Supporting Data for “Thermal Expansion and Isotope Effects of Chemical Shift of C60-Fullerene Using Machine Learning-Assisted Path Integral Molecular Dynamics”. *figshare. Dataset.* [DOI: TBA]

---

For further details, please refer to the respective folders or contact the author via the provided email.
