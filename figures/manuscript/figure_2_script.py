import numpy as np
import matplotlib.pyplot as plt

# Initialize the figure and subplots
fig = plt.figure(layout='none', figsize=(12, 8))
ax1 = fig.add_subplot(241)
ax11 = fig.add_subplot(242)
ax2 = fig.add_subplot(243)
ax22 = fig.add_subplot(244)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# Remove unnecessary features from the figure
ax1.spines['right'].set_visible(False)
ax11.spines['left'].set_visible(False)
ax11.yaxis.set_visible(False)

ax2.spines['right'].set_visible(False)
ax22.spines['left'].set_visible(False)
ax22.yaxis.set_visible(False)

fig.subplots_adjust(left=0.118, right=0.985, wspace=0.25, top=0.955, bottom=0.1, hspace=0.274)

# Load predicted and DFT energy values (train and test) and print some key values of the data
energy_test = np.loadtxt('log/MLIP-1/energy_test.out')[:, 0]
energy_train = np.loadtxt('log/MLIP-1/energy_train.out')[:, 0]
energy_test_true = np.loadtxt('log/MLIP-1/energy_test.out')[:, 1]
energy_train_true = np.loadtxt('log/MLIP-1/energy_train.out')[:, 1]
print("MLIP-1 energy train MAE: ", np.average(np.absolute(energy_train-energy_train_true))*1000)
print("MLIP-1 energy test MAE: ", np.average(np.absolute(energy_test-energy_test_true))*1000)
print("\n")
energy_test_m2 = np.loadtxt('log/MLIP-2/energy_test.out')[:, 0]
energy_train_m2 = np.loadtxt('log/MLIP-2/energy_train.out')[:, 0]
energy_test_true_m2 = np.loadtxt('log/MLIP-2/energy_test.out')[:, 1]
energy_train_true_m2 = np.loadtxt('log/MLIP-2/energy_train.out')[:, 1]
print("MLIP-2 energy train MAE: ", np.average(np.absolute(energy_train_m2-energy_train_true_m2))*1000)
print("MLIP-2 energy test MAE: ", np.average(np.absolute(energy_test_m2-energy_test_true_m2))*1000)
print("\n")
energy_test_m3 = np.loadtxt('log/MLIP-3/energy_test.out')[:, 0]
energy_train_m3 = np.loadtxt('log/MLIP-3/energy_train.out')[:, 0]
energy_test_true_m3 = np.loadtxt('log/MLIP-3/energy_test.out')[:, 1]
energy_train_true_m3 = np.loadtxt('log/MLIP-3/energy_train.out')[:, 1]
print("MLIP-3 energy train MAE: ", np.average(np.absolute(energy_train_m3-energy_train_true_m3))*1000)
print("MLIP-3 energy test MAE: ", np.average(np.absolute(energy_test_m3-energy_test_true_m3))*1000)
print("\n")

# Load force predicted components
force_test_x = np.loadtxt('log/MLIP-1/force_test.out')[:, 0]
force_train_x = np.loadtxt('log/MLIP-1/force_train.out')[:, 0]
force_test_y = np.loadtxt('log/MLIP-1/force_test.out')[:, 1]
force_train_y = np.loadtxt('log/MLIP-1/force_train.out')[:, 1]
force_test_z = np.loadtxt('log/MLIP-1/force_test.out')[:, 2]
force_train_z = np.loadtxt('log/MLIP-1/force_train.out')[:, 2]

force_test_x_m2 = np.loadtxt('log/MLIP-2/force_test.out')[:, 0]
force_train_x_m2 = np.loadtxt('log/MLIP-2/force_train.out')[:, 0]
force_test_y_m2 = np.loadtxt('log/MLIP-2/force_test.out')[:, 1]
force_train_y_m2 = np.loadtxt('log/MLIP-2/force_train.out')[:, 1]
force_test_z_m2 = np.loadtxt('log/MLIP-2/force_test.out')[:, 2]
force_train_z_m2 = np.loadtxt('log/MLIP-2/force_train.out')[:, 2]

force_test_x_m3 = np.loadtxt('log/MLIP-3/force_test.out')[:, 0]
force_train_x_m3 = np.loadtxt('log/MLIP-3/force_train.out')[:, 0]
force_test_y_m3 = np.loadtxt('log/MLIP-3/force_test.out')[:, 1]
force_train_y_m3 = np.loadtxt('log/MLIP-3/force_train.out')[:, 1]
force_test_z_m3 = np.loadtxt('log/MLIP-3/force_test.out')[:, 2]
force_train_z_m3 = np.loadtxt('log/MLIP-3/force_train.out')[:, 2]

# Load DFT force components
force_test_x_true = np.loadtxt('log/MLIP-1/force_test.out')[:, 3]
force_train_x_true = np.loadtxt('log/MLIP-1/force_train.out')[:, 3]
force_test_y_true = np.loadtxt('log/MLIP-1/force_test.out')[:, 4]
force_train_y_true = np.loadtxt('log/MLIP-1/force_train.out')[:, 4]
force_test_z_true = np.loadtxt('log/MLIP-1/force_test.out')[:, 5]
force_train_z_true = np.loadtxt('log/MLIP-1/force_train.out')[:, 5]

force_test_x_true_m2 = np.loadtxt('log/MLIP-2/force_test.out')[:, 3]
force_train_x_true_m2 = np.loadtxt('log/MLIP-2/force_train.out')[:, 3]
force_test_y_true_m2 = np.loadtxt('log/MLIP-2/force_test.out')[:, 4]
force_train_y_true_m2 = np.loadtxt('log/MLIP-2/force_train.out')[:, 4]
force_test_z_true_m2 = np.loadtxt('log/MLIP-2/force_test.out')[:, 5]
force_train_z_true_m2 = np.loadtxt('log/MLIP-2/force_train.out')[:, 5]

force_test_x_true_m3 = np.loadtxt('log/MLIP-3/force_test.out')[:, 3]
force_train_x_true_m3 = np.loadtxt('log/MLIP-3/force_train.out')[:, 3]
force_test_y_true_m3 = np.loadtxt('log/MLIP-3/force_test.out')[:, 4]
force_train_y_true_m3 = np.loadtxt('log/MLIP-3/force_train.out')[:, 4]
force_test_z_true_m3 = np.loadtxt('log/MLIP-3/force_test.out')[:, 5]
force_train_z_true_m3 = np.loadtxt('log/MLIP-3/force_train.out')[:, 5]

# Print key values of the data
print("MLIP-1 force train MAE: ", (np.average(np.absolute(force_train_x-force_train_x_true)) + np.average(np.absolute(force_train_y-force_train_y_true)) + np.average(np.absolute(force_train_z-force_train_z_true)))/3)
print("MLIP-1 force test MAE: ", (np.average(np.absolute(force_test_x-force_test_x_true)) + np.average(np.absolute(force_test_y-force_test_y_true)) + np.average(np.absolute(force_test_z-force_test_z_true)))/3)
print("\n")
print("MLIP-2 force train MAE: ", (np.average(np.absolute(force_train_x_m2-force_train_x_true_m2)) + np.average(np.absolute(force_train_y_m2-force_train_y_true_m2)) + np.average(np.absolute(force_train_z_m2-force_train_z_true_m2)))/3)
print("MLIP-2 force test MAE: ", (np.average(np.absolute(force_test_x_m2-force_test_x_true_m2)) + np.average(np.absolute(force_test_y_m2-force_test_y_true_m2)) + np.average(np.absolute(force_test_z_m2-force_test_z_true_m2)))/3)
print("\n")
print("MLIP-3 force train MAE: ", (np.average(np.absolute(force_train_x_m3-force_train_x_true_m3)) + np.average(np.absolute(force_train_y_m3-force_train_y_true_m3)) + np.average(np.absolute(force_train_z_m3-force_train_z_true_m3)))/3)
print("MLIP-3 force test MAE: ", (np.average(np.absolute(force_test_x_m3-force_test_x_true_m3)) + np.average(np.absolute(force_test_y_m3-force_test_y_true_m3)) + np.average(np.absolute(force_test_z_m3-force_test_z_true_m3)))/3)

# Combine force components in a numpy array
force_test_comb = np.concatenate((force_test_x, force_test_y, force_test_z), axis=None)
force_train_comb = np.concatenate((force_train_x, force_train_y, force_train_z), axis=None)

force_test_comb_true = np.concatenate((force_test_x_true, force_test_y_true, force_test_z_true), axis=None)
force_train_comb_true = np.concatenate((force_train_x_true, force_train_y_true, force_train_z_true), axis=None)


force_test_comb_m2 = np.concatenate((force_test_x_m2, force_test_y_m2, force_test_z_m2), axis=None)
force_train_comb_m2 = np.concatenate((force_train_x_m2, force_train_y_m2, force_train_z_m2), axis=None)

force_test_comb_true_m2 = np.concatenate((force_test_x_true_m2, force_test_y_true_m2, force_test_z_true_m2), axis=None)
force_train_comb_true_m2 = np.concatenate((force_train_x_true_m2, force_train_y_true_m2, force_train_z_true_m2), axis=None)

force_test_comb_m3 = np.concatenate((force_test_x_m3, force_test_y_m3, force_test_z_m3), axis=None)
force_train_comb_m3 = np.concatenate((force_train_x_m3, force_train_y_m3, force_train_z_m3), axis=None)

force_test_comb_true_m3 = np.concatenate((force_test_x_true_m3, force_test_y_true_m3, force_test_z_true_m3), axis=None)
force_train_comb_true_m3 = np.concatenate((force_train_x_true_m3, force_train_y_true_m3, force_train_z_true_m3), axis=None)


# Plot the figures
plot1 = ax1.hist(energy_train_true, 10, facecolor='blue', alpha=0.8, label="Train m1", edgecolor='black', linewidth=0.5)
plot1_2 = ax1.hist(energy_train_true_m2, 10, facecolor='green', alpha=0.8, label="Train m2", edgecolor='black', linewidth=0.5)
plot1_3 = ax1.hist(energy_train_true_m3, 10, facecolor='red', alpha=0.8, label="Train m3", edgecolor='black', linewidth=0.5)
ax1.set_ylabel('Number of datapoints', fontsize=20)
ax1.set_xlabel(r'                             $E_{DFT}$ (eV/atom)', fontsize=20)
ax1.set_xlim(-1.49, -1.33)
ax1.set_xticks([-1.45, -1.35])
ax1.tick_params(axis='x', labelsize=20)
ax1.tick_params(axis='y', labelsize=20)

plot11 = ax11.hist(energy_train_true, 10, facecolor='blue', alpha=0.8, label="Train m1", edgecolor='black', linewidth=0.5)
plot11_2 = ax11.hist(energy_train_true_m2, 10, facecolor='green', alpha=0.8, label="Train m2", edgecolor='black', linewidth=0.5)
plot11_3 = ax11.hist(energy_train_true_m3, 10, facecolor='red', alpha=0.8, label="Train m3", edgecolor='black', linewidth=0.5)
ax11.set_xlim(-0.52, -0.43)
ax11.set_xticks([-0.5, -0.45])
ax11.tick_params(axis='x', labelsize=20)
ax11.tick_params(axis='y', labelsize=20)

plot2 = ax2.hist(energy_test_true, 10, facecolor='blue', alpha=0.8, label="Test m1", edgecolor='black', linewidth=0.5)
plot2_2 = ax2.hist(energy_test_true_m2, 10, facecolor='green', alpha=0.8, label="Test m2", edgecolor='black', linewidth=0.5)
plot2_3 = ax2.hist(energy_test_true_m3, 10, facecolor='red', alpha=0.8, label="Test m3", edgecolor='black', linewidth=0.5)
ax2.set_xlabel(r'                             $E_{DFT}$ (eV/atom)', fontsize=20)
ax2.set_xlim(-1.49, -1.33)
ax2.set_xticks([-1.45, -1.35])
ax2.tick_params(axis='x', labelsize=20)
ax2.tick_params(axis='y', labelsize=20)

plot22 = ax22.hist(energy_test_true, 10, facecolor='blue', alpha=0.8, label="Test m1", edgecolor='black', linewidth=0.5)
plot22_2 = ax22.hist(energy_test_true_m2, 10, facecolor='green', alpha=0.8, label="Test m2", edgecolor='black', linewidth=0.5)
plot22_3 = ax22.hist(energy_test_true_m3, 10, facecolor='red', alpha=0.8, label="Test m3", edgecolor='black', linewidth=0.5)
ax22.set_xlim(-0.52, -0.43)
ax22.set_xticks([-0.5, -0.45])
ax22.tick_params(axis='x', labelsize=20)
ax22.tick_params(axis='y', labelsize=20)
ax22.legend(["DFT-1", "DFT-2", "DFT-3"], loc="upper right", fontsize=18)

plot3 = ax3.hist(force_train_comb_true, 15, alpha=0.7, facecolor='blue', edgecolor='blue', linewidth=2, histtype='step')
plot3_2 = ax3.hist(force_train_comb_true_m2, 15, alpha=0.7, facecolor='green', edgecolor='green', linewidth=2, histtype='step')
plot3_3 = ax3.hist(force_train_comb_true_m3, 15, alpha=0.7, facecolor='red', edgecolor='red', linewidth=2, histtype='step')
ax3.set_ylabel('Number of datapoints', fontsize=20)
ax3.set_xlabel(r'$F_{DFT}$ (eV/Å)', fontsize=20)
ax3.tick_params(axis='x', labelsize=20)
ax3.tick_params(axis='y', labelsize=20)

plot4 = ax4.hist(force_test_comb_true, 15, facecolor='blue', alpha=0.7, edgecolor='blue', linewidth=2, histtype='step')
plot4_2 = ax4.hist(force_test_comb_true_m2, 15, facecolor='green', alpha=0.7, edgecolor='green', linewidth=2, histtype='step')
plot4_3 = ax4.hist(force_test_comb_true_m3, 15, facecolor='red', alpha=0.7, edgecolor='red', linewidth=2, histtype='step')
ax4.set_xlabel(r'$F_{DFT}$ (eV/Å)', fontsize=20)
ax4.tick_params(axis='x', labelsize=20)
ax4.tick_params(axis='y', labelsize=20)


# Make the breaklines in the axes
d1 = -1  # proportion of vertical to horizontal extent of the slanted line
kwargs_bottom = dict(marker=[(-d1, -1), (d1, 1)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax11.plot([0, -0.19], [0, 0], transform=ax11.transAxes, **kwargs_bottom)
ax22.plot([0, -0.19], [0, 0], transform=ax22.transAxes, **kwargs_bottom)

d2 = -1  # proportion of vertical to horizontal extent of the slanted line
kwargs_top = dict(marker=[(-d2, -1), (d2, 1)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)

# Plot the broken axis lines
ax11.plot([0, -0.19], [1, 1], transform=ax11.transAxes, **kwargs_top)
ax22.plot([0, -0.19], [1, 1], transform=ax22.transAxes, **kwargs_top)


plt.savefig('figure_2.png', dpi=300)
plt.show()
