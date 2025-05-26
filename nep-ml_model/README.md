This folder contains all the needed input files to train a NEP MLIP model

# C<sub>60</sub> NEP3 Machine learning interatomic potentials (MLIP)

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---

## Training process of NEP3 model

Training of a NEP model requires the input file `nep.in` and the training and testing dataset xyz-files `train.xyz` and `test.xyz`.
The internal hyperparameters and the training process are controlled through the `nep.in` input file.
With the provided file structure, the training process of NEP can be started with the command `nep`, provided that **GPUMD** and **NEP** are installed.

