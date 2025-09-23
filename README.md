# Supporting Code for “*Machine Learning-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene*”

## Graphical Abstract

![Graphical Abstract](./blank.png)

---

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [Academic Portfolio](https://ozakary.github.io/)

---

This is the supporting code for the manuscript “***Machine Learning-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene***”. [DOI: TBA]

The repository comprises the following sections:

1. Dataset preparation for the three MLIP models:  
   i. Configuration generation using semi-empirical MD simulations. ([directory](./dftb-md/))  
   ii. DFT calculations of the generated SE-MD configurations for training the three MLIP models. ([directory](./dft_calculations_nep/))  
   iii. Dataset format of the MLIP models. ([directory](./nep-ml_dataset/))  
3. Example of training, validation, and testing processes for a MLIP model using NEP3 architecture. ([directory](./nep-ml_model/))  
4. Machine learning-assisted path-integral MD simulations. ([directory](./pimd_simulations/))  
5. Dataset preparation for the NMR-ML model:  
   i. Configuration generation using semi-empirical MD simulations. ([directory](./dftb-md/))  
   ii. DFT calculations for the NMR-ML model. ([directory](./dft_calculations_schnet/))  
   iii. Dataset format for the NMR-ML model. ([directory](./nmr-ml_dataset/))  
6. Training, validation, and testing processes for the NMR-ML model using SchNet architecture on NMR magnetic shielding parameters, including the skew, span, and σ<sub>iso</sub>. ([directory](./nmr-ml_model/))  
7. Prediction of NMR isotropic magnetic shielding values, σ<sub>iso</sub>, from the pre-trained NMR-ML model. ([directory](./nmr-ml_prediction/))  
8. Python scripts and raw numerical data for all figures related to the NMR-ML model included in the main manuscript and the Supporting Information. ([directory](./figures/))  

## Citations
If you use this data, please cite the following:

### Preprint

```bibtex
@article{laurila2025_ml_c60,
  title={Machine Learning-Enabled Insights Into Quantum Effects on Structure and $^{13}$C NMR of C$_{60}$ Fullerene},
  author={Laurila, Ossi, and Jacklin, Tiia, and Zakary, Ouail and Lantto, Perttu},
  journal={In preparation},
  year={2025},
  note={DOI: To be announced}
}
```

### Dataset

```bibtex
@dataset{laurila2025_data_c60,
  author = {Laurila, Ossi, and Jacklin, Tiia, and Zakary, Ouail and Lantto, Perttu},
  title = {Supporting Data for "Machine Learning-Enabled Insights Into Quantum Effects on Structure and $^{13}$C NMR of C$_{60}$ Fullerene"},
  year = {2025},
  publisher = {In preparation},
  note = {DOI: To be announced},
}
```

---
For further details, please refer to the respective folders or contact the author via the provided email.
