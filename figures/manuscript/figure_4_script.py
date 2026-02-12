import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, layout='none', figsize=(14, 7))

fig.subplots_adjust(left=0.074, right=0.945, wspace=0.257, top=0.954, bottom=0.082, hspace=0.244)

# Load energy results of MLIP-1
energy_test_m1 = np.loadtxt('log/MLIP-1/energy_test.out')
energy_train_m1 = np.loadtxt('log/MLIP-1/energy_train.out')

# Load energy results of MLIP-2
energy_test_m2 = np.loadtxt('log/MLIP-2/energy_test.out')
energy_train_m2 = np.loadtxt('log/MLIP-2/energy_train.out')

# Load energy results of MLIP-3
energy_test_m3 = np.loadtxt('log/MLIP-3/energy_test.out')
energy_train_m3 = np.loadtxt('log/MLIP-3/energy_train.out')

# Load force results of MLIP-1
force_test_m1 = np.loadtxt('log/MLIP-1/force_test.out')
force_train_m1 = np.loadtxt('log/MLIP-1/force_train.out')

# Load force results of MLIP-2
force_test_m2 = np.loadtxt('log/MLIP-2/force_test.out')
force_train_m2 = np.loadtxt('log/MLIP-2/force_train.out')

# Load force results of MLIP-3
force_test_m3 = np.loadtxt('log/MLIP-3/force_test.out')
force_train_m3 = np.loadtxt('log/MLIP-3/force_train.out')

# Extract the data of predicted force components
force_test_comb_m1 = np.concatenate((force_test_m1[:, 0], force_test_m1[:, 1], force_test_m1[:, 2]), axis=None)
force_train_comb_m1 = np.concatenate((force_train_m1[:, 0], force_train_m1[:, 1], force_train_m1[:, 2]), axis=None)

force_test_comb_m2 = np.concatenate((force_test_m2[:, 0], force_test_m2[:, 1], force_test_m2[:, 2]), axis=None)
force_train_comb_m2 = np.concatenate((force_train_m2[:, 0], force_train_m2[:, 1], force_train_m2[:, 2]), axis=None)

force_test_comb_m3 = np.concatenate((force_test_m3[:, 0], force_test_m3[:, 1], force_test_m3[:, 2]), axis=None)
force_train_comb_m3 = np.concatenate((force_train_m3[:, 0], force_train_m3[:, 1], force_train_m3[:, 2]), axis=None)


# Extract the data of DFT force components
force_test_comb_m1_true = np.concatenate((force_test_m1[:, 3], force_test_m1[:, 4], force_test_m1[:, 5]), axis=None)
force_train_comb_m1_true = np.concatenate((force_train_m1[:, 3], force_train_m1[:, 4], force_train_m1[:, 5]), axis=None)

force_test_comb_m2_true = np.concatenate((force_test_m2[:, 3], force_test_m2[:, 4], force_test_m2[:, 5]), axis=None)
force_train_comb_m2_true = np.concatenate((force_train_m2[:, 3], force_train_m2[:, 4], force_train_m2[:, 5]), axis=None)

force_test_comb_m3_true = np.concatenate((force_test_m3[:, 3], force_test_m3[:, 4], force_test_m3[:, 5]), axis=None)
force_train_comb_m3_true = np.concatenate((force_train_m3[:, 3], force_train_m3[:, 4], force_train_m3[:, 5]), axis=None)

#MLIP-1 energy correlation plot
slope_e_test_m1, intercept_e_test_m1, r_value_e_test_m1, p_value_e_test_m1, std_err_e_test_m1 = stats.linregress(energy_test_m1[:, 1], energy_test_m1[:, 0])
ax1.scatter(60*energy_train_m1[:, 1], 60*energy_train_m1[:, 0], marker='o', alpha=0.4, color='blue', label="Train")
ax1.scatter(60*energy_test_m1[:, 1], 60*energy_test_m1[:, 0], marker= 'x', alpha=0.4, color='darkorange', label="Test")
ax1.plot(np.linspace(-1.489*60, -1.425*60), np.linspace(-1.489*60, -1.425*60), 'r-', alpha=0.8)
ax1.set_xlabel(r'$E_{\text{DFT}}$ (eV)', fontsize=13)
ax1.set_ylabel(r'$E_{\text{ML}}$ (eV)', fontsize=13, x=-2.0)
ax1.set_xticks([-1.48*60, -1.46*60, -1.44*60])
ax1.set_yticks([-1.48*60, -1.46*60, -1.44*60])
ax1.text(.04, .91, f'train. RMSE = 11.4 meV/C$_{{60}}$', fontsize=12, transform=ax1.transAxes)
ax1.text(.04, .83, f'valid. RMSE = 11.4 meV/C$_{{60}}$', fontsize=12, transform=ax1.transAxes)
ax1.text(.04, .75, f'valid. R$^2$ = {r_value_e_test_m1**2:.4f}', fontsize=12, transform=ax1.transAxes)
ax1.tick_params(axis='x', labelsize=13)
ax1.tick_params(axis='y', labelsize=13)
ax1.legend(["train.", "valid."], loc="lower right", fontsize=13, framealpha=1)
ax1.set_title("MLIP-1.2", fontsize=13)
ax1.set_xlim([-1.489*60, -1.425*60])
ax1.set_ylim([-1.489*60, -1.425*60])

#MLIP-2 energy correlation plot
slope_e_test_m2, intercept_e_test_m2, r_value_e_test_m2, p_value_e_test_m2, std_err_e_test_m2 = stats.linregress(energy_test_m2[:, 1], energy_test_m2[:, 0])
ax2.scatter(60*energy_train_m2[:, 1], 60*energy_train_m2[:, 0], marker = 'o', alpha=0.4, color='blue')
ax2.scatter(60*energy_test_m2[:, 1], 60*energy_test_m2[:, 0], marker = 'x', alpha=0.4, color='darkorange')
ax2.plot(np.linspace(-1.4*60, -1.335*60), np.linspace(-1.4*60, -1.335*60), 'r-', alpha=0.8)
ax2.set_xlabel(r'$E_{\text{DFT}}$ (eV)', fontsize=13)
ax2.set_xticks([-1.39*60, -1.37*60, -1.35*60])
ax2.set_yticks([-1.39*60, -1.37*60, -1.35*60])
ax2.text(.04, .91, f'train. RMSE = 12.0 meV/C$_{{60}}$', fontsize=12, transform=ax2.transAxes)
ax2.text(.04, .83, f'valid. RMSE = 12.0 meV/C$_{{60}}$', fontsize=12, transform=ax2.transAxes)
ax2.text(.04, .75, f'valid. R$^2$ = {r_value_e_test_m2**2:.4f}', fontsize=12, transform=ax2.transAxes)
ax2.tick_params(axis='x', labelsize=13)
ax2.tick_params(axis='y', labelsize=13)
ax2.set_title("MLIP-2", fontsize=13)
ax2.set_xlim([-1.4*60, -1.335*60])
ax2.set_ylim([-1.4*60, -1.335*60])

#MLIP-3 energy correlation plot
slope_e_test_m3, intercept_e_test_m3, r_value_e_test_m3, p_value_e_test_m3, std_err_e_test_m3 = stats.linregress(energy_test_m3[:, 1], energy_test_m3[:, 0])
ax3.scatter(60*energy_train_m3[:, 1], 60*energy_train_m3[:, 0], marker = 'o', alpha=0.4, color='blue')
ax3.scatter(60*energy_test_m3[:, 1], 60*energy_test_m3[:, 0], marker = 'x', alpha=0.4, color='darkorange')
ax3.plot(np.linspace(-0.503*60, -0.437*60), np.linspace(-0.503*60, -0.437*60), 'r-', alpha=0.8)
ax3.set_xlabel(r'$E_{\text{DFT}}$ (eV)', fontsize=13)
ax3.set_xticks([-0.5*60, -0.48*60, -0.46*60, -0.44*60])
ax3.set_yticks([-0.5*60, -0.48*60, -0.46*60, -0.44*60])
ax3.text(.04, .91, f'train. RMSE = 10.8 meV/C$_{{60}}$', fontsize=12, transform=ax3.transAxes)
ax3.text(.04, .83, f'valid. RMSE = 13.2 meV/C$_{{60}}$', fontsize=12, transform=ax3.transAxes)
ax3.text(.04, .75, f'valid. R$^2$ = {r_value_e_test_m3**2:.4f}', fontsize=12, transform=ax3.transAxes)
ax3.tick_params(axis='x', labelsize=13)
ax3.tick_params(axis='y', labelsize=13)
ax3.set_title("MLIP-3", fontsize=13)
ax3.set_xlim([-0.503*60, -0.437*60])
ax3.set_ylim([-0.503*60, -0.437*60])

#MLIP-1 force correlation plot
slope_f_test_m1, intercept_f_test_m1, r_value_f_test_m1, p_value_f_test_m1, std_err_f_test_m1 = stats.linregress(force_test_comb_m1_true, force_test_comb_m1)
ax4.scatter(force_train_m1[:, 3:6], force_train_m1[:, 0:3], marker = 'o', alpha=0.4, color='blue', label="Train")
ax4.scatter(force_test_m1[:, 3:6], force_test_m1[:, 0:3], marker = 'x', alpha=0.4, color='darkorange', label="Test")
ax4.plot(np.linspace(-10,10), np.linspace(-10,10), 'r-', alpha=0.8)
ax4.set_xlabel(r'$\vec f_{\text{DFT}}$ (eV/Å)', fontsize=13)
ax4.set_ylabel(r'$\vec f_{\text{ML}}$ (eV/Å)', fontsize=13, x=-2.0)
ax4.text(0.05, 0.91, 'train. RMSE = 0.0432 eV/Å', fontsize=12, transform=ax4.transAxes)
ax4.text(0.05, 0.83, 'valid. RMSE = 0.0435 eV/Å', fontsize=12, transform=ax4.transAxes)
ax4.text(0.05, 0.75, f'valid. R$^2$ = {r_value_f_test_m1**2:.4f}', fontsize=12, transform=ax4.transAxes)
ax4.tick_params(axis='x', labelsize=13)
ax4.tick_params(axis='y', labelsize=13)
ax4.set_xlim([-10, 10])
ax4.set_ylim([-10, 10])

#MLIP-2 force correlation plot
slope_f_test_m2, intercept_f_test_m2, r_value_f_test_m2, p_value_f_test_m2, std_err_f_test_m2 = stats.linregress(force_test_comb_m2_true, force_test_comb_m2)
ax5.scatter(force_train_m2[:, 3:6], force_train_m2[:, 0:3], marker = 'o', alpha=0.4, color='blue')
ax5.scatter(force_test_m2[:, 3:6], force_test_m2[:, 0:3], marker = 'x', alpha=0.4, color='darkorange')
ax5.plot(np.linspace(-10,10), np.linspace(-10,10), 'r-', alpha=0.8)
ax5.set_xlabel(r'$\vec f_{\text{DFT}}$ (eV/Å)', fontsize=13)
ax5.text(0.05, 0.90, 'train. RMSE = 0.0430 eV/Å', fontsize=12, transform=ax5.transAxes)
ax5.text(0.05, 0.82, 'valid. RMSE = 0.0448 eV/Å', fontsize=12, transform=ax5.transAxes)
ax5.text(0.05, 0.74, f'valid. R$^2$ = {r_value_f_test_m2**2:.4f}', fontsize=12, transform=ax5.transAxes)
ax5.tick_params(axis='x', labelsize=13)
ax5.tick_params(axis='y', labelsize=13)
ax5.set_xlim([-10, 10])
ax5.set_ylim([-10, 10])

#MLIP-3 force correlation plot
slope_f_test_m3, intercept_f_test_m3, r_value_f_test_m3, p_value_f_test_m3, std_err_f_test_m3 = stats.linregress(force_test_comb_m3_true, force_test_comb_m3)
ax6.scatter(force_train_m3[:, 3:6], force_train_m3[:, 0:3], marker = 'o', alpha=0.4, color='blue')
ax6.scatter(force_test_m3[:, 3:6], force_test_m3[:, 0:3], marker = 'x', alpha=0.4, color='darkorange')
ax6.plot(np.linspace(-10,10), np.linspace(-10,10), 'r-', alpha=0.8)
ax6.set_xlabel(r'$\vec f_{\text{DFT}}$ (eV/Å)', fontsize=13)
ax6.text(0.05, 0.90, 'train. RMSE = 0.0452 eV/Å', fontsize=12, transform=ax6.transAxes)
ax6.text(0.05, 0.82, 'valid. RMSE = 0.0463 eV/Å', fontsize=12, transform=ax6.transAxes)
ax6.text(0.05, 0.74, f'valid. R$^2$ = {r_value_f_test_m3**2:.4f}', fontsize=12, transform=ax6.transAxes)
ax6.tick_params(axis='x', labelsize=13)
ax6.tick_params(axis='y', labelsize=13)
ax6.set_xlim([-10, 10])
ax6.set_ylim([-10, 10])

plt.savefig('figure_4.png', dpi=300)
plt.show()
