# He@C<sub>60</sub> semi-empirical MD with DFTB+ code

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---

## Producing the reference dataset structures of C<sub>60</sub>

This directory contains the necessary input files to reproduce the semi-empirical MD data with DFTB+ software. The configurations of the output MD trajectory are used as reference data in the training of NEP3 MLIP models and SchNet NMR-ML model.

### Input files

All the necessary files needed to start the MD simulation with DFTB+ are provided in the [input_files](./input_files) directory. The structure of the directory is as follows:
```
./
     dftb_in.hsd        # The main input file for DFTB+
     dftb_pin.hsd       # Processed and parsed input file created by the DFTB+ software, preferred over dftb_in.hsd to repeat the simulation
     geom.out.gen       # The initial He@C<sub>60</sub> configuration in the generic format
     geom.out.xyz       # The initial He@C<sub>60</sub> configuration in the xyz format
```

- Note that if you want to exactly repeat the calculation, you are strongly suggested to remove the `dftb_in.hsd`, and then rename the file `dftb_pin.hsd` as `dftb_in.hsd`.


### Scripts

Scripts used to analyze the MD trajectory and to initialize the [DFT calculations](../dft_calculations_nep) for the C<sub>60</sub> structures produced in the MD simulation are presented in the [scripts](./scripts) directory.  

**prepare.sh**  
After the DFTB+ calculation has been completed this shell script prepares the results for the DFT calculations of the reference C<sub>60</sub> configurations.  
Running the script with the command `./prepare.sh` creates the following file structure:
```
./cluster_0
    coord_0.xyz
    createC60xyz.py
./cluster_1
    coord_1.xyz
    createC60xyz.py
...
./cluster_1
    coord_1.xyz
    createC60xyz.py
```

**createC60xyz.py**  
This Python script removes the helium atom from the center of the He@C<sub>60</sub> endofullerene end produced an empty C<sub>60</sub> structure.

---

For further details, please refer to the original [DFTB+]([https://github.com/brucefan1983/GPUMD](https://github.com/dftbplus/dftbplus)) documentation or contact the author via the provided email.
