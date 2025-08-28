import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#Load data of simulation in folder f and split the data at interval s
def ld(f, s):
    return np.concatenate(np.loadtxt('./' + f + '/allvol.txt')[0::s], axis=None)

#Calculate mean and stdev and standard error
def calc_stats(data):
    means = []
    devs = []
    sems = []
    for el in data:
        means.append(np.round(np.mean(el), 3))
        devs.append(np.round(np.std(el), 3))
        sems.append(np.round(np.std(el)/(len(el))**(1/2), 4))
    return means, devs, sems

# Load the data
volumedata_m1 = [ld('./MLIP-1/80K', 1),
              ld('./MLIP-1/100K', 1),
              ld('./MLIP-1/120K', 1),
              ld('./MLIP-1/150K', 1),
              ld('./MLIP-1/200K', 1),
              ld('./MLIP-1/250K', 1),
              ld('./MLIP-1/300K', 1),
              ld('./MLIP-1/350K', 1),
              ld('./MLIP-1/400K', 1),
              ld('./MLIP-1/500K', 1)]

volumedata_m2 = [ld('./MLIP-2/100K', 1),
              ld('./MLIP-2/150K', 1),
              ld('./MLIP-2/200K', 1),
              ld('./MLIP-2/250K', 1),
              ld('./MLIP-2/300K', 1),
              ld('./MLIP-2/350K', 1),
              ld('./MLIP-2/400K', 1),
              ld('./MLIP-2/500K', 1)]

volumedata_m3 = [ld('./MLIP-3/100K', 1),
              ld('./MLIP-3/150K', 1),
              ld('./MLIP-3/200K', 1),
              ld('./MLIP-3/250K', 1),
              ld('./MLIP-3/300K', 1),
              ld('./MLIP-3/350K', 1),
              ld('./MLIP-3/400K', 1),
              ld('./MLIP-3/500K', 1)]

# Reference data (rovibrational)
volumedata_ref = [186.06196, 186.062138, 186.06203, 186.06126, 186.05835, 186.05472, 186.05244, 186.05340, 186.058889, 186.08564]

# Define the simulated temperatures
temps = [80, 100, 120, 150, 200, 250, 300, 350, 400, 500]
m2_3_temps = [100, 150, 200, 250, 300, 350, 400, 500]

# Calculate statistics for all three model data
m1_data, m1_data_std, m1_data_sem = calc_stats(volumedata_m1)
m2_data, m2_data_std, m2_data_sem = calc_stats(volumedata_m2)
m3_data, m3_data_std, m3_data_sem = calc_stats(volumedata_m3)


# Calculate the volume difference wrt to volume at 150 K
m1_data_abs_diff = [a - m1_data[3] for a in m1_data]
m2_data_abs_diff = [a - m2_data[1] for a in m2_data]
m3_data_abs_diff = [a - m3_data[1] for a in m3_data]
ref_data_abs_diff = [a - volumedata_ref[3] for a in volumedata_ref]

# Plot the data

fig, (ax1, ax2) = plt.subplots(1, 2, layout='none', figsize=(12.4, 5))
fig.subplots_adjust(left=0.105, right=0.952, wspace=0.5, top=0.921, bottom=0.117, hspace=0.2)

ax1.scatter(temps, m1_data, color='black', s=22)
ax1.errorbar(temps, m1_data, yerr=m1_data_sem, capsize=2.0, marker="o", markersize=7, color='black', linestyle="solid")
ax1.errorbar(m2_3_temps, m2_data, yerr=m2_data_sem, capsize=2.0, marker="v", markersize=7, color='blue', linestyle="dotted")
ax1.errorbar(m2_3_temps, m3_data, yerr=m3_data_sem, capsize=2.0, marker="d", markersize=7, color='orange', linestyle="dashed")
ax1.errorbar(temps, volumedata_ref, yerr=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], capsize=0, marker='x', markersize=7, color='green', linestyle="dashdot")
ax1.set_xlabel('T (K)', fontsize=13)
ax1.set_ylabel(r'Absolute volume ($Å^3$)', fontsize=13)
ax1.tick_params(axis='x', labelsize=13)
ax1.tick_params(axis='y', labelsize=13)
ax1.grid(True)

err2 = ax2.errorbar(m2_3_temps, m2_data_abs_diff, yerr=m2_data_sem, capsize=2.0, marker="v", markersize=7, color='blue', label='MLIP-2', linestyle="dotted")
err3 = ax2.errorbar(m2_3_temps, m3_data_abs_diff, yerr=m3_data_sem, capsize=2.0, marker="d", markersize=7, color='orange', label='MLIP-3', linestyle="dashed")
err4 = ax2.errorbar(temps, ref_data_abs_diff, yerr=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], capsize=0, marker='x', markersize=7, color='green', label ='Rovibrational data', linestyle="dashdot")
err1 = ax2.errorbar(temps, m1_data_abs_diff, yerr=m1_data_sem, capsize=2.0, marker="o", markersize=7, color='black', label='MLIP-1', linestyle="solid")
ax2.set_xlabel('T (K)', fontsize=13)
ax2.set_ylabel(r'Absolute volume $V$(T) - $V$(150 K) ($Å^3$)', fontsize=13)
ax2.set_ylim([-0.02, 0.12])
ax2.tick_params(axis='x', labelsize=13)
ax2.tick_params(axis='y', labelsize=13)
ax2.legend(handles=[err1, err2, err3, err4], loc="upper center", fontsize=11, ncols=2, framealpha=1)
ax2.grid(True)


# Print some results
print("MLIP-1:")
for i in range(len(volumedata_m1)):
    print(str(temps[i]) + 'K avg volume = ' + str(m1_data[i]) + ' and std = ' + str(m1_data_std[i]) + ' and SEM: ' + str(m1_data_sem[i]) + " data: " + str(len(volumedata_m1[i])))

print("\n" + "MLIP-2:")
for i in range(len(volumedata_m2)):
    print(str(m2_3_temps[i]) + 'K avg volume = ' + str(m2_data[i]) + ' and std = ' + str(m2_data_std[i]) + ' and SEM: ' + str(m2_data_sem[i]) + " data: " + str(len(volumedata_m2[i])))

print("\n" + "MLIP-3:")
for i in range(len(volumedata_m3)):
    print(str(m2_3_temps[i]) + 'K avg volume = ' + str(m3_data[i]) + ' and std = ' + str(m3_data_std[i]) + ' and SEM: ' + str(m3_data_sem[i]) + " data: " + str(len(volumedata_m3[i])))

plt.savefig('figure_7.png', dpi=300)
plt.show()
