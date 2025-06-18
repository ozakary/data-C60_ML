# C<sub>60</sub> NEP3 Machine Learning Interatomic Potentials (MLIP)

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---

## Training process of NEP3 model

The training process of a NEP model is briefly described here.

### Input files

Training of a NEP model requires the input file `nep.in` to specify the hyperparameters, and the training and testing dataset xyz-files `train.xyz` and `test.xyz`.
```
./
  nep.in      # Hyperparameters of the trained model are specified here
  train.xyz   # Training dataset configurations
  test.xyz    # Testing dataset configurations
```

The internal hyperparameters of the model and the training process are controlled through the `nep.in` input file.
With the provided file structure, the training process of NEP model may be started simply with the command
```nep```
provided that **GPUMD** and **NEP** are installed.  
Here we have only provided truncated `train.xyz` and `test.xyz` files as an example. The actual files used to train the models **MLIP-1**, **MLIP-2**, and **MLIP-3** can be found [here](../dft_calculations_nep), or in the external `Zenodo` [repository](https://github.com/ozakary/data-NMR-ML_C60).

### Output files

The training process creates the following output files:
```
./
  energy_test.out        # Predicted values of energy for structures in test.xyz
  energy_train.out       # Predicted values of energy for structures in train.xyz
  force_test.out         # Predicted values of forces for structures in test.xyz
  force_train.out        # Predicted values of forces for structures in train.xyz
  loss.out               # Values of loss function terms during the training process logged every 100th generation
  nep.txt                # The trained model parameter file
  nep.restart            # Restart file
  run_results.out        # Log file of the training
  run_error.out          # Error file of the training
```

- Note that we do not use virials in the training process
- All trained NEP model parameter files are available [here](../pimd_simulations/pimd_nte), or in the external `Zenodo` [repository](https://github.com/ozakary/data-NMR-ML_C60).
- In the [output_files](./output_files) directory, the output files of the training process (generations 600 000 - 800 000) of the MLIP-1 model are provided.

---

For further details, please refer to the original [GPUMD](https://github.com/brucefan1983/GPUMD) documentation or contact the author via the provided email.
