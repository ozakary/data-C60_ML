import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, layout='none', figsize=(14, 7))

fig.subplots_adjust(left=0.074, right=0.945, wspace=0.257, top=0.954, bottom=0.082, hspace=0.244)

# Load energy results of MLIP-1
energy_test_m1 = np.loadtxt('MLIP-1/energy_test.out')
energy_train_m1 = np.loadtxt('MLIP-1/energy_train.out')

# Load energy results of MLIP-2
energy_test_m2 = np.loadtxt('MLIP-2/energy_test.out')
energy_train_m2 = np.loadtxt('MLIP-2/energy_train.out')

# Load energy results of MLIP-3
energy_test_m3 = np.loadtxt('MLIP-3/energy_test.out')
energy_train_m3 = np.loadtxt('MLIP-3/energy_train.out')

# Load force results of MLIP-1
force_test_m1 = np.loadtxt('MLIP-1/force_test.out')
force_train_m1 = np.loadtxt('MLIP-1/force_train.out')

# Load force results of MLIP-2
force_test_m2 = np.loadtxt('MLIP-2/force_test.out')
force_train_m2 = np.loadtxt('MLIP-2/force_train.out')

# Load force results of MLIP-3
force_test_m3 = np.loadtxt('MLIP-3/force_test.out')
force_train_m3 = np.loadtxt('MLIP-3/force_train.out')

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
ax1.scatter(energy_train_m1[:, 1], energy_train_m1[:, 0], marker='o', alpha=0.4, color='blue', label="Train")
ax1.scatter(energy_test_m1[:, 1], energy_test_m1[:, 0], marker= 'x', alpha=0.4, color='darkorange', label="Test")
ax1.plot(np.linspace(-1.489, -1.425), np.linspace(-1.489, -1.425), 'r-', alpha=0.8)
ax1.set_xlabel('DFT energy (meV/atom)', fontsize=13)
ax1.set_ylabel('NEP energy (meV/atom)', fontsize=13, x=-2.0)
ax1.set_xticks([-1.48, -1.46, -1.44])
ax1.set_yticks([-1.48, -1.46, -1.44])
ax1.text(0.05, 0.90, 'Train RMSE = 0.19', fontsize=12, transform=ax1.transAxes)
ax1.text(0.05, 0.82, 'Test RMSE = 0.19', fontsize=12, transform=ax1.transAxes)
ax1.text(0.05, 0.74, f'Test R$^2$ = {r_value_e_test_m1**2:.3f}', fontsize=12, transform=ax1.transAxes)
ax1.tick_params(axis='x', labelsize=13)
ax1.tick_params(axis='y', labelsize=13)
ax1.legend(["Train", "Test"], loc="lower right", fontsize=13, framealpha=1)
ax1.set_title("MLIP-1", fontsize=13)
ax1.set_xlim([-1.489, -1.425])
ax1.set_ylim([-1.489, -1.425])

#MLIP-2 energy correlation plot
slope_e_test_m2, intercept_e_test_m2, r_value_e_test_m2, p_value_e_test_m2, std_err_e_test_m2 = stats.linregress(energy_test_m2[:, 1], energy_test_m2[:, 0])
ax2.scatter(energy_train_m2[:, 1], energy_train_m2[:, 0], marker = 'o', alpha=0.4, color='blue')
ax2.scatter(energy_test_m2[:, 1], energy_test_m2[:, 0], marker = 'x', alpha=0.4, color='darkorange')
ax2.plot(np.linspace(-1.4, -1.335), np.linspace(-1.4, -1.335), 'r-', alpha=0.8)
ax2.set_xlabel('DFT energy (meV/atom)', fontsize=13)
ax2.set_xticks([-1.39, -1.37, -1.35])
ax2.set_yticks([-1.39, -1.37, -1.35])
ax2.text(0.05, 0.90, 'Test RMSE = 0.20', fontsize=12, transform=ax2.transAxes)
ax2.text(0.05, 0.82, 'Test RMSE = 0.20', fontsize=12, transform=ax2.transAxes)
ax2.text(0.05, 0.74, f'Train R$^2$ = {r_value_e_test_m2**2:.3f}', fontsize=12, transform=ax2.transAxes)
ax2.tick_params(axis='x', labelsize=13)
ax2.tick_params(axis='y', labelsize=13)
ax2.set_title("MLIP-2", fontsize=13)
ax2.set_xlim([-1.4, -1.335])
ax2.set_ylim([-1.4, -1.335])

#MLIP-3 energy correlation plot
slope_e_test_m3, intercept_e_test_m3, r_value_e_test_m3, p_value_e_test_m3, std_err_e_test_m3 = stats.linregress(energy_test_m3[:, 1], energy_test_m3[:, 0])
ax3.scatter(energy_train_m3[:, 1], energy_train_m3[:, 0], marker = 'o', alpha=0.4, color='blue')
ax3.scatter(energy_test_m3[:, 1], energy_test_m3[:, 0], marker = 'x', alpha=0.4, color='darkorange')
ax3.plot(np.linspace(-0.503, -0.437), np.linspace(-0.503, -0.437), 'r-', alpha=0.8)
ax3.set_xlabel('DFT energy (meV/atom)', fontsize=13)
ax3.set_xticks([-0.5, -0.48, -0.46, -0.44])
ax3.set_yticks([-0.5, -0.48, -0.46, -0.44])
ax3.text(0.05, 0.90, 'Train RMSE = 0.18', fontsize=12, transform=ax3.transAxes)
ax3.text(0.05, 0.82, 'Test RMSE = 0.22', fontsize=12, transform=ax3.transAxes)
ax3.text(0.05, 0.74, f'Test R$^2$ = {r_value_e_test_m3**2:.3f}', fontsize=12, transform=ax3.transAxes)
ax3.tick_params(axis='x', labelsize=13)
ax3.tick_params(axis='y', labelsize=13)
ax3.set_title("MLIP-3", fontsize=13)
ax3.set_xlim([-0.503, -0.437])
ax3.set_ylim([-0.503, -0.437])

#MLIP-1 force correlation plot
slope_f_test_m1, intercept_f_test_m1, r_value_f_test_m1, p_value_f_test_m1, std_err_f_test_m1 = stats.linregress(force_test_comb_m1_true, force_test_comb_m1)
ax4.scatter(force_train_m1[:, 3:6], force_train_m1[:, 0:3], marker = 'o', alpha=0.4, color='blue', label="Train")
ax4.scatter(force_test_m1[:, 3:6], force_test_m1[:, 0:3], marker = 'x', alpha=0.4, color='darkorange', label="Test")
ax4.plot(np.linspace(-10,10), np.linspace(-10,10), 'r-', alpha=0.8)
ax4.set_xlabel('DFT force (eV/Å)', fontsize=13)
ax4.set_ylabel('NEP force (eV/Å)', fontsize=13, x=-2.0)
ax4.text(0.05, 0.90, 'Train RMSE = 0.0432', fontsize=12, transform=ax4.transAxes)
ax4.text(0.05, 0.82, 'Test RMSE = 0.0435', fontsize=12, transform=ax4.transAxes)
ax4.text(0.05, 0.74, f'Test R$^2$ = {r_value_f_test_m1**2:.3f}', fontsize=12, transform=ax4.transAxes)
ax4.tick_params(axis='x', labelsize=13)
ax4.tick_params(axis='y', labelsize=13)
ax4.set_xlim([-10, 10])
ax4.set_ylim([-10, 10])

#MLIP-2 force correlation plot
slope_f_test_m2, intercept_f_test_m2, r_value_f_test_m2, p_value_f_test_m2, std_err_f_test_m2 = stats.linregress(force_test_comb_m2_true, force_test_comb_m2)
ax5.scatter(force_train_m2[:, 3:6], force_train_m2[:, 0:3], marker = 'o', alpha=0.4, color='blue')
ax5.scatter(force_test_m2[:, 3:6], force_test_m2[:, 0:3], marker = 'x', alpha=0.4, color='darkorange')
ax5.plot(np.linspace(-10,10), np.linspace(-10,10), 'r-', alpha=0.8)
ax5.set_xlabel('DFT force (eV/Å)', fontsize=13)
ax5.text(0.05, 0.90, 'Train RMSE = 0.0430', fontsize=12, transform=ax5.transAxes)
ax5.text(0.05, 0.82, 'Test RMSE = 0.0448', fontsize=12, transform=ax5.transAxes)
ax5.text(0.05, 0.74, f'Test R$^2$ = {r_value_f_test_m2**2:.3f}', fontsize=12, transform=ax5.transAxes)
ax5.tick_params(axis='x', labelsize=13)
ax5.tick_params(axis='y', labelsize=13)
ax5.set_xlim([-10, 10])
ax5.set_ylim([-10, 10])

#MLIP-3 force correlation plot
slope_f_test_m3, intercept_f_test_m3, r_value_f_test_m3, p_value_f_test_m3, std_err_f_test_m3 = stats.linregress(force_test_comb_m3_true, force_test_comb_m3)
ax6.scatter(force_train_m3[:, 3:6], force_train_m3[:, 0:3], marker = 'o', alpha=0.4, color='blue')
ax6.scatter(force_test_m3[:, 3:6], force_test_m3[:, 0:3], marker = 'x', alpha=0.4, color='darkorange')
ax6.plot(np.linspace(-10,10), np.linspace(-10,10), 'r-', alpha=0.8)
ax6.set_xlabel('DFT force (eV/Å)', fontsize=13)
ax6.text(0.05, 0.90, 'Train RMSE = 0.0452', fontsize=12, transform=ax6.transAxes)
ax6.text(0.05, 0.82, 'Test RMSE = 0.0463', fontsize=12, transform=ax6.transAxes)
ax6.text(0.05, 0.74, f'Test R$^2$ = {r_value_f_test_m3**2:.3f}', fontsize=12, transform=ax6.transAxes)
ax6.tick_params(axis='x', labelsize=13)
ax6.tick_params(axis='y', labelsize=13)
ax6.set_xlim([-10, 10])
ax6.set_ylim([-10, 10])

plt.savefig('figure_3.png', dpi=300, transparent=True)
plt.show()
