# Supporting Data for “*Neural Networks-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene*”

## Graphical Abstract

![Graphical Abstract](./blank.png)

---

📄 Authors: **Ouail Zakary** and **Ossi Laurila**

---

👤 Corresponding Author: **Ouail Zakary**  
- 📧 Email: [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
- 🔗 ORCID: [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
- 🌐 Website: [Personal Webpage](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)  
- 📁 Portfolio: [GitHub Portfolio](https://ozakary.github.io/)

---

This is the Supporting Dataset for the manuscript “***Neural Networks-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene***”. [DOI: TBA]

The dataset comprises the following sections:

1. Dataset preparation for the three MLIP models:  
   i. Configuration generation using semi-empirical MD simulations. ([directory](./dftb-md/))  
   ii. DFT calculations of the generated SE-MD configurations for training the three MLIP models. ([directory](./dft_calculations_nep/))  
2. Example of training, validation, and testing processes for a MLIP model using NEP3 architecture. ([directory](./nep-ml_model/))  
3. Machine learning-assisted path-integral MD simulations. ([directory](./pimd_simulations/))  
4. Dataset preparation for the NMR-ML model:  
   i. Configuration generation using semi-empirical MD simulations. ([directory](./dftb-md/))  
   ii. DFT calculations for the NMR-ML model. ([directory](./dft_calculations_schnet/))  
   iii. Dataset format for the NMR-ML model. ([directory](./nmr-ml_dataset/))  
5. Training, validation, and testing processes for the NMR-ML model using SchNet architecture on NMR magnetic shielding parameters, including the skew, span, and σ<sub>iso</sub>. ([directory](./nmr-ml_model/))  
6. Prediction of NMR isotropic magnetic shielding values, σ<sub>iso</sub>, from the pre-trained NMR-ML model. ([directory](./nmr-ml_prediction/))  
7. Python scripts and raw numerical data for all figures related to the NMR-ML model included in the main manuscript and the Supporting Information. ([directory](./figures/))  

## Citations

If you use this data, please cite the following: \
\
**Paper:** Laurila O.; Jacklin T.; Zakary, O.; Lantto P. Neural Networks-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene. *In preparation* **2025**. [DOI: TBA]

\
**Dataset:** Laurila O.; Jacklin T.; Zakary, O.; Lantto P. (**2025**). Supporting Data for “Neural Networks-Enabled Insights Into Quantum Effects on Structure and <sup>13</sup>C NMR of C<sub>60</sub> Fullerene”. *Zenodo. Dataset.* [DOI: TBA]

---

For further details, please refer to the respective folders or contact the author via the provided email.
