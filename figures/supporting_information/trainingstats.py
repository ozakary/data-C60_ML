import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Load the data
loss_m1 = np.loadtxt('../manuscript/MLIP-1/loss.out')
loss_m2 = np.loadtxt('../manuscript/MLIP-2/loss.out')
loss_m3 = np.loadtxt('../manuscript/MLIP-3/loss.out')

energy_train_m1 = loss_m1[:6000, 4]*1000
force_train_m1 = loss_m1[:6000, 5]

energy_train_m2 = loss_m2[:, 4]*1000
force_train_m2 = loss_m2[:, 5]

energy_train_m3 = loss_m3[:, 4]*1000
force_train_m3 = loss_m3[:, 5]

#Plot
plt.rcParams.update({'font.size': 16})
fig, (ax1, ax2) = plt.subplots(1, 2, layout='none', figsize=(11, 5))
fig.subplots_adjust(left=0.08, right=0.968, wspace=0.387, top=0.921, bottom=0.117, hspace=0.2)

#Energy train
ax1.loglog(energy_train_m1, color='blue', label="MLIP-1")
ax1.loglog(energy_train_m2, color='green', label="MLIP-2")
ax1.loglog(energy_train_m3, color='orange', label="MLIP-3")
ax1.set_xlabel('Training generation/100', fontsize=14)
ax1.set_ylabel('Energy loss (meV/atom)', fontsize=14)
ax1.set_yticks([0.2, 0.5, 1.0, 2.0])
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.tick_params(axis='x', labelsize=14)
ax1.tick_params(axis='y', labelsize=14)
ax1.legend(loc="upper right", fontsize=13)
ax1.grid(True, which="both", ls="-", alpha=0.2)

#Force train
ax2.loglog(force_train_m1, color='blue', label="MLIP-1")
ax2.loglog(force_train_m2, color='green', label="MLIP-2")
ax2.loglog(force_train_m3, color='orange', label="MLIP-3")
ax2.set_xlabel('Training generation/100', fontsize=14)
ax2.set_ylabel('Force loss (eV/Å)', fontsize=14)
ax2.set_yticks([0.05, 0.1, 0.2, 0.3])
ax2.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax2.tick_params(axis='x', labelsize=14)
ax2.tick_params(axis='y', labelsize=14)
ax2.legend(loc="upper right", fontsize=13)
ax2.grid(True, which="both", ls="-", alpha=0.2)

plt.savefig('figure_S5.png', dpi=300, transparent=True)
plt.show()
