# Machine Learning-Assisted Path Integral Molecular Dynamics (MLAPIMD) Simulations

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---
This sub-repository contains example input files for the PIMD simulations, final NEP MLIP potential/parameter files, and workflow of the PIMD simulations of C<sub>60</sub> with [GPUMD](https://github.com/brucefan1983/GPUMD) code. 

One example PIMD simulation run with the resulting output files for the C<sub>60</sub> NTE study and the C<sub>60</sub> NMR study is provided in the [IDA repository](https://github.com/ozakary/data-NMR-ML_C60) of the project. Due to the massive size of the whole PIMD simulation data, it is not possible to provide everything in the IDA repository.

## Directory Structure


### PIMD for NMR chemical shielding
Three sub-directories are provided  
- [pimd_nmr_hh](./pimd_nmr_hh)
- [pimd_nmr_hp](./pimd_nmr_hp)
- [pimd_nmr_single](./pimd_nmr_single)  

The structure of each directory is:

```
./
    model.xyz             # Input structure of C60 for the initial configuration of the simulation
    nep.txt               # The trained NEP model MLIP-1, containing the trained parameters of the model
    run.in                # Simulation protocol
```

### PIMD for NTE of C<sub>60</sub>
A directory [pimd_nmr_nte](./pimd_nte) is provided with the following structure:

```
./
    model.xyz              # An example input structure of C60 for the initial configuration of the simulation
    nep-mlip1.txt          # The trained NEP model MLIP-1, containing the trained parameters of the model
    nep-mlip2.txt          # The trained NEP model MLIP-2, containing the trained parameters of the model
    nep-mlip3.txt          # The trained NEP model MLIP-3, containing the trained parameters of the model
    run.in                 # Simulation protocol
    volume_avg.py          # Script for calculating the average volume of C60 over the beads
    volume_beads.py        # Script for calculating the volume of each individual bead
```

***volume_beads.py***  
Python script `volume_beads.py` calculates for each bead **\<i\>** in the PIMD simulation the volume of C<sub>60</sub> from the samples written in the file beads_dump_\<i\>.xyz. The script creates the output files:

```
./
     volumes_0bead.txt
     volumes_1bead.txt
     volumes_(P-1)bead.txt
```
Here ``P`` is the number of beads used in the simulation. Each line in the output file volumes_ell_\<i\>bead.txt contains the volume of C<sub>60</sub> calculated from the bead **\<i\>** of the simulation, with the format:
```
<0>:<volume (Å)>
<1>:<volume (Å)>
...
<n>:<volume (Å)>
````
Here ``<n>``is the n<sup>th</sup> output structure in the beads_dump_\<i\>.xyz output file.


***volume_avg.py***  
Python script `volume_avg.py` calculates the average volume of C<sub>60</sub> configuration by taking the average of the volume over all the beads written in the files volumes_ell_\<i\>bead.txt. The script creates an output file `volumes_ell_average.txt`, with the format:
```
<volume (Å)>
<volume (Å)>
...
```
Here each line in the file contains the average volume of C<sub>60</sub> calculated from the corresponding lines in the files volumes_ell_\<i\>bead.txt.


## Workflow
Necessary files to start PIMD simulation with [GPUMD](https://github.com/brucefan1983/GPUMD) code are `model.xyz`, `nep.txt`, and `run.in`.

1. Install [GPUMD](https://github.com/brucefan1983/GPUMD)
2. Check and modify the simulation protocol file `run.in`
3. Start the simulation with the command `gpumd`
4. To calculate the volume of C<sub>60</sub> samples from the xyz-files, run the python scripts: 
```
python3 volume_beads.py
python3 volume_avg.py
```

In the case of PIMD for NMR chemical shielding, the step 4 may be skipped. In this case the analysis can be continued with the instructions found in [nmr-ml_prediction](../nmr-ml_prediction).


---

For further details, please contact the author via the provided email.
