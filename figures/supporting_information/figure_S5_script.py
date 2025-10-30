import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.formatter.useoffset'] = False
plt.rcParams['axes.formatter.use_locale'] = False
plt.rcParams['axes.formatter.limits'] = (-10, 10)  # effectively disables sci notation

# Load the data
loss_m1 = np.loadtxt('./log/MLIP-1/loss.out')
loss_m2 = np.loadtxt('./log/MLIP-2/loss.out')
loss_m3 = np.loadtxt('./log/MLIP-3/loss.out')

energy_train_m1 = loss_m1[:6000, 4]*1000
force_train_m1 = loss_m1[:6000, 5]

energy_train_m2 = loss_m2[:, 4]*1000
force_train_m2 = loss_m2[:, 5]

energy_train_m3 = loss_m3[:, 4]*1000
force_train_m3 = loss_m3[:, 5]

energy_val_m1 = loss_m1[:6000, 7]*1000
force_val_m1 = loss_m1[:6000, 8]

energy_val_m2 = loss_m2[:, 7]*1000
force_val_m2 = loss_m2[:, 8]

energy_val_m3 = loss_m3[:, 7]*1000
force_val_m3 = loss_m3[:, 8]

#Plot
plt.rcParams.update({'font.size': 16})
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, layout='none', figsize=(12, 7))
fig.subplots_adjust(left=0.08, right=0.968, wspace=0.387, top=0.921, bottom=0.117, hspace=0.2)

#Energy train
ax1.loglog(energy_train_m1, color='blue', label="MLIP-1.2 training")
ax1.loglog(energy_val_m1, color='green', label="MLIP-1.2 validation")
ax1.set_ylabel('Energy loss (meV/atom)', fontsize=14)
ax1.set_yticks([0.2, 0.5, 1.0, 2.0])
ax1.set_xticks([1, 10, 100, 1000, 10000])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax1.set_xlim([10, 14000])
ax1.legend(loc="upper right", fontsize=12)
ax1.grid(True, which="both", axis="both", ls="-", alpha=0.4)

ax2.loglog(energy_train_m2, color='blue', label="MLIP-2 training")
ax2.loglog(energy_val_m2, color='green', label="MLIP-2 validation")
ax2.set_yticks([0.2, 0.5, 1.0, 2.0])
ax2.set_xticks([1, 10, 100, 1000, 10000])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.tick_params(axis='x', labelsize=14)
ax2.tick_params(axis='y', labelsize=14)
ax2.set_xlim([10, 14000])
ax2.legend(loc="upper right", fontsize=12)
ax2.grid(True, which="both", axis="both", ls="-", alpha=0.4)

ax3.loglog(energy_train_m3, color='blue', label="MLIP-3 training")
ax3.loglog(energy_val_m3, color='green', label="MLIP-3 validation")
ax3.set_yticks([0.2, 0.5, 1.0, 2.0])
ax3.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax3.tick_params(axis='x', labelsize=14)
ax3.tick_params(axis='y', labelsize=14)
ax3.set_xlim([10, 20000])
ax3.legend(loc="upper right", fontsize=12)
ax3.grid(True, which="both", axis="both", ls="-", alpha=0.4)

#Force train
ax4.loglog(force_train_m1, color='blue', label="MLIP-1.2 training")
ax4.loglog(force_val_m1, color='green', label="MLIP-1.2 validation")
ax4.set_xlabel('Training iteration/100', fontsize=14)
ax4.set_ylabel('Force loss (eV/Å)', fontsize=14)
ax4.set_yticks([0.05, 0.1, 0.2, 0.3])
ax4.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax4.tick_params(axis='x', labelsize=14)
ax4.tick_params(axis='y', labelsize=14)
ax4.set_xlim([10, 14000])
ax4.set_ylim([0.03, 0.32])
ax4.legend(loc="upper right", fontsize=12)
ax4.grid(True, which="both", axis="both", ls="-", alpha=0.4)

ax5.loglog(force_train_m2, color='blue', label="MLIP-2 training")
ax5.loglog(force_val_m2, color='green', label="MLIP-2 validation")
ax5.set_xlabel('Training iteration/100', fontsize=14)
ax5.set_yticks([0.05, 0.1, 0.2, 0.3])
ax5.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax5.tick_params(axis='x', labelsize=14)
ax5.tick_params(axis='y', labelsize=14)
ax5.set_xlim([10, 14000])
ax5.set_ylim([0.03, 0.32])
ax5.legend(loc="upper right", fontsize=12)
ax5.grid(True, which="both", axis="both", ls="-", alpha=0.4)

ax6.loglog(force_train_m3, color='blue', label="MLIP-3 training")
ax6.loglog(force_val_m3, color='green', label="MLIP-3 validation")
ax6.set_xlabel('Training iteration/100', fontsize=14)
ax6.set_yticks([0.05, 0.1, 0.2, 0.3])
ax6.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax6.tick_params(axis='x', labelsize=14)
ax6.tick_params(axis='y', labelsize=14)
ax6.set_xlim([10, 20000])
ax6.set_ylim([0.03, 0.32])
ax6.legend(loc="upper right", fontsize=12)
ax6.grid(True, which="both", axis="both", ls="-", alpha=0.4)

plt.savefig('figure_S5.png', dpi=300)
plt.show()
