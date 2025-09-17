# He@C<sub>60</sub> Semi-Empirical MD Using DFTB+ Code

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

## Producing the reference dataset structures of C<sub>60</sub>

This directory contains the necessary input files to reproduce the semi-empirical MD data with DFTB+ software. The configurations of the output MD trajectory are used as reference data in the training of NEP3 MLIP models and SchNet NMR-ML model. The output files, including the full trajectory of the semi-empirical MD simulation can be found in the [IDA repository](https://github.com/ozakary/data-NMR-ML_C60) of this project.

### DFTB+ input files

All the necessary files needed to start the MD simulation with DFTB+ are provided here. The structure of the directory is as follows:
```
./
     dftb_in.hsd        # The main input file for DFTB+
     dftb_pin.hsd       # Processed and parsed input file created by the DFTB+ software, preferred over dftb_in.hsd to repeat the simulation
     geom.out.gen       # The initial He@C60 configuration in the generic format
     geom.out.xyz       # The initial He@C60 configuration in the xyz format
     puhti_dftb.job     # Job script to run DFTB+ in Puhti HPC
     prepare.sh         # Shell script for preparing DFT calculations, not used in DFTB+ simulation
     createC60xyz.py    # Python script used to create empty C60 structures from the DFTB+ simulation trajectory of He@C60
```

- Note that if you want to exactly repeat the calculation, you are strongly suggested to remove the `dftb_in.hsd`, and then rename the file `dftb_pin.hsd` as `dftb_in.hsd`  
- The additional script files `prepare.sh` and `createC60xyz.py` are used after the DFTB+ simulation has finished to extract sample C<sub>60</sub> structure configurations from the simulation trajectory.


### Scripts

Scripts used to analyze the MD trajectory and to initialize the [DFT calculations](../dft_calculations_nep) for the C<sub>60</sub> structures produced in the MD simulation are presented below.  

**prepare.sh**  

After the DFTB+ calculation has been completed this shell script prepares the results for the DFT calculations of the reference C<sub>60</sub> configurations.  
Running the script with the command `./prepare.sh` creates the following file structure:
```
./cluster_34000
    coord_34000.xyz
    createC60xyz.py
./cluster_34500
    coord_34500.xyz
    createC60xyz.py
./cluster_35000
    coord_35000.xyz
    createC60xyz.py
...
```
Note that the first selected configuration is `cluster_34000`, since the beginning of the semi-empirical MD simulation is discarded due to the equilibration stage of the simulation.

Follow the instruction in [dft_calculations_nep](../dft_calculations_nep) or [dft_calculations_schnet](../dft_calculations_schnet) to run the DFT calculations for the C<sub>60</sub> configurations.

**createC60xyz.py**  

This Python script removes the helium atom from the center of the He@C<sub>60</sub> endofullerene, producing an empty C<sub>60</sub> structure.

---

For further details, please refer to the original [DFTB+]([https://github.com/brucefan1983/GPUMD](https://github.com/dftbplus/dftbplus)) documentation or contact the author via the provided email.
