import numpy as np
import matplotlib.pyplot as plt


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout='none', figsize=(9, 7))

fig.subplots_adjust(left=0.129, right=0.955, wspace=0.274, top=0.955, bottom=0.1, hspace=0.274)

# Load predicted and DFT energy values (train and test)
energy_test = np.loadtxt('MLIP-1/energy_test.out')[:, 0]
energy_train = np.loadtxt('MLIP-1/energy_train.out')[:, 0]
energy_test_true = np.loadtxt('MLIP-1/energy_test.out')[:, 1]
energy_train_true = np.loadtxt('MLIP-1/energy_train.out')[:, 1]

# Load force predicted components
force_test_x = np.loadtxt('MLIP-1/force_test.out')[:, 0]
force_train_x = np.loadtxt('MLIP-1/force_train.out')[:, 0]
force_test_y = np.loadtxt('MLIP-1/force_test.out')[:, 1]
force_train_y = np.loadtxt('MLIP-1/force_train.out')[:, 1]
force_test_z = np.loadtxt('MLIP-1/force_test.out')[:, 2]
force_train_z = np.loadtxt('MLIP-1/force_train.out')[:, 2]

# Load DFT force components
force_test_x_true = np.loadtxt('MLIP-1/force_test.out')[:, 3]
force_train_x_true = np.loadtxt('MLIP-1/force_train.out')[:, 3]
force_test_y_true = np.loadtxt('MLIP-1/force_test.out')[:, 4]
force_train_y_true = np.loadtxt('MLIP-1/force_train.out')[:, 4]
force_test_z_true = np.loadtxt('MLIP-1/force_test.out')[:, 5]
force_train_z_true = np.loadtxt('MLIP-1/force_train.out')[:, 5]

# Combine force components in a numpy array
force_test_comb = np.concatenate((force_test_x, force_test_y, force_test_z), axis=None)
force_train_comb = np.concatenate((force_train_x, force_train_y, force_train_z), axis=None)

force_test_comb_true = np.concatenate((force_test_x_true, force_test_y_true, force_test_z_true), axis=None)
force_train_comb_true = np.concatenate((force_train_x_true, force_train_y_true, force_train_z_true), axis=None)


# Plot the figures
plot1 = ax1.hist(energy_train_true, 15, facecolor='blue', alpha=0.75, label="Train")
ax1.set_ylabel('Number of datapoints', fontsize=16)
ax1.set_xlabel(r'$E_{DFT}$ (eV/atom)', fontsize=16)
ax1.set_xticks([-1.48, -1.46, -1.44])
ax1.tick_params(axis='x', labelsize=16)
ax1.tick_params(axis='y', labelsize=16)
ax1.legend(["Train"], loc="upper right", fontsize=12, framealpha=0)

plot2 = ax2.hist(energy_test_true, 15, facecolor='darkorange', alpha=0.75, label="Test")
ax2.set_xlabel(r'$E_{DFT}$ (eV/atom)', fontsize=16)
ax2.set_xticks([-1.48, -1.46, -1.44])
ax2.tick_params(axis='x', labelsize=16)
ax2.tick_params(axis='y', labelsize=16)
ax2.legend(["Test"], loc="upper right", fontsize=12, framealpha=0)

plot3 = ax3.hist(force_train_comb_true, 15, facecolor='blue', alpha=0.75)
ax3.set_ylabel('Number of datapoints', fontsize=16)
ax3.set_xlabel(r'$F_{DFT}$ (eV/Å)', fontsize=16)
ax3.tick_params(axis='x', labelsize=16)
ax3.tick_params(axis='y', labelsize=16)

plot4 = ax4.hist(force_test_comb_true, 15, facecolor='darkorange', alpha=0.75)
ax4.set_xlabel(r'$F_{DFT}$ (eV/Å)', fontsize=16)
ax4.tick_params(axis='x', labelsize=16)
ax4.tick_params(axis='y', labelsize=16)


plt.savefig('reference_data_nep.png', dpi=300)
plt.show()
