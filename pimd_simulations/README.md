# Path integral molecular dynamics (PIMD) simulations

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---
This sub-repository contains the input files and workflow for our PIMD simulations of C<sub>60</sub> with [GPUMD](https://github.com/brucefan1983/GPUMD) code.

## Directory Structure

Four sub-directories [pimd_nmr_hh](./pimd_nmr_hh), [pimd_nmr_hp](./pimd_nmr_hp), [pimd_nmr_single](./pimd_nmr_single), [pimd_nmr_nte](./pimd_nmr_nte) are provided, each with the structure

```
./
    model.xyz             # Input structure of C<sub>60</sub> for the initial configuration of the simulation
    nep.txt               # The trained NEP MLIP, containing the trained parameters of the model
    run.in                # Simulation protocol
```


## Script Files
```
./nmr-ml_train-valid-test_script.py                 # Main Python script for model training
./nmr-ml_schnet_carpo2.job                # SLURM job submission script
```

### Output Files (the output files, including the NMR-ML trained model are to be found in this [Zenodo repository](https://github.com/ozakary/data-NMR-ML_C60))
```
./beads_dump_0.xyz            # Contains the trajectory data of bead 0
./beads_dump_1.xyz            # Contains the trajectory data of bead 1
...
./beads_dump_(n-1).xyz        # Contains the trajectory data of bead n-1
./dump.xyz                    # Contains the trajectory data of the centroid of the ring polymer
./neighbor.out                # Contains neighbor information of the descriptors
./run_results.out             # Log-file of the simulation
./run_error.out               # Error log-file of the simulation
./thermo.out                  # Contains thermodynamic quantities sampled during the simulation
```

---

For further details, please refer to the respective folders or contact the author via the provided email.
