import numpy as np
import matplotlib.pyplot as plt
from ase.units import kcal, mol
import pandas as pd

# Linestyle settings of matplotlib
linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 5))),
     ('densely dotted',        (0, (1, 1))),

     ('long dash with offset', (5, (10, 3))),
     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]


#Load data of simulation in folder f and split the data at interval s
def ld(f, s):
    try:
        return np.concatenate(np.loadtxt('./' + f + '/allvol.txt')[::s], axis=None)
    except FileNotFoundError:
        return np.concatenate(np.loadtxt('./' + f + '/volumes_trace.txt')[0::s], axis=None)

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
volumes_1bead = [ld('100K/1b', 1), ld('150K/1b', 1), ld('200K/1b', 1), ld('250K/1b', 1), 
                ld('300K/1b', 1), ld('350K/1b', 1), ld('400K/1b', 1), ld('500K/1b', 1)]

volumes_2bead = [ld('100K/2b', 1), ld('150K/2b', 1), ld('200K/2b', 1), ld('250K/2b', 1), 
                ld('300K/2b', 1), ld('350K/2b', 1), ld('400K/2b', 1), ld('500K/2b', 1)]


volumes_4bead = [ld('100K/4b', 1), ld('150K/4b', 1), ld('200K/4b', 1), ld('250K/4b', 1), 
                ld('300K/4b', 1), ld('350K/4b', 1), ld('400K/4b', 1), ld('500K/4b', 1)]


volumes_8bead = [ld('100K/8b', 2), ld('150K/8b', 2), ld('200K/8b', 2), ld('250K/8b', 2), 
                ld('300K/8b', 2), ld('350K/8b', 2), ld('400K/8b', 2), ld('500K/8b', 2)]


volumes_16bead = [ld('100K/16b', 3), ld('150K/16b', 3), ld('200K/16b', 3), ld('250K/16b', 3), 
                ld('300K/16b', 3), ld('350K/16b', 3), ld('400K/16b', 3), ld('500K/16b', 3)]


volumes_32bead = [ld('100K/32b', 3), ld('150K/32b', 3), ld('200K/32b', 3), ld('250K/32b', 3), 
                ld('300K/32b', 3), ld('350K/32b', 3), ld('400K/32b', 2), ld('500K/32b', 2)]


volumes_64bead = [ld('100K/64b', 2), ld('150K/64b', 2), ld('200K/64b', 2), ld('250K/64b', 1), 
                ld('300K/64b', 1), ld('350K/64b', 2)]


volumes_128bead = [ld('100K/128b', 2), ld('150K/128b', 2), ld('200K/128b', 2), ld('250K/128b', 2)]

# Calculate staistics of the data
vol_1bead, std_1bead, sem_1bead = calc_stats(volumes_1bead)
vol_2bead, std_2bead, sem_2bead = calc_stats(volumes_2bead)
vol_4bead, std_4bead, sem_4bead = calc_stats(volumes_4bead)
vol_8bead, std_8bead, sem_8bead = calc_stats(volumes_8bead)
vol_16bead, std_16bead, sem_16bead = calc_stats(volumes_16bead)
vol_32bead, std_32bead, sem_32bead = calc_stats(volumes_32bead)
vol_64bead, std_64bead, sem_64bead = calc_stats(volumes_64bead)
vol_128bead, std_128bead, sem_128bead = calc_stats(volumes_128bead)

# x-axis
temps = [100, 150, 200, 250, 300, 350, 400, 500]

# Plot the data
fig, ax = plt.subplots(figsize=(8, 7))
fig.subplots_adjust(left=0.144, right=0.943, wspace=0.533, top=0.843, bottom=0.099)

plt.rcParams.update({'font.size': 16})

ax.scatter(temps, vol_1bead, color='green', alpha=0.65, s=22)
err1 = ax.errorbar(temps, vol_1bead, label="P=1", yerr=sem_1bead, capsize=2.0, fmt="o", color='green', markersize=6, marker="o", linestyle="solid")
ax.scatter(temps, vol_2bead, color='#ba9500', alpha=0.65, s=22)
err2 = ax.errorbar(temps, vol_2bead, label="P=2", yerr=sem_2bead, capsize=2.0, fmt="o", color='#ba9500', markersize=6, marker="v", linestyle="dotted")
ax.scatter(temps, vol_4bead, color='#2dad76', alpha=0.65, s=22)
err3 = ax.errorbar(temps, vol_4bead, label="P=4", yerr=sem_4bead, capsize=2.0, fmt="o", color='#2dad76', markersize=6, marker="d", linestyle="dashed")
ax.scatter(temps, vol_8bead, color='blue', alpha=0.65, s=22)
err4 = ax.errorbar(temps, vol_8bead, label="P=8", yerr=sem_8bead, capsize=2.0, fmt="o", color='blue', markersize=6, marker="s", linestyle="dashdot")
ax.scatter(temps, vol_16bead, color='#00439c', alpha=0.65, s=22)
err5 = ax.errorbar(temps, vol_16bead, label="P=16", yerr=sem_16bead, capsize=2.0, fmt="o", color='#00439c', markersize=6, marker="P", linestyle=(0, (5, 1)))
ax.scatter(temps, vol_32bead, color='purple', alpha=0.65, s=22)
err6 = ax.errorbar(temps, vol_32bead, label="P=32", yerr=sem_32bead, capsize=2.0, fmt="o", color='purple', markersize=6, marker="*", linestyle=(5, (10, 3)))
ax.scatter(temps[0:6], vol_64bead, color='#520202', alpha=0.65, s=22)
err7 = ax.errorbar(temps[0:6], vol_64bead, label="P=64", yerr=sem_64bead, capsize=2.0, fmt="o", color='#520202', markersize=6, marker="p", linestyle=(0, (3, 1, 1, 1)))
ax.scatter(temps[0:4], vol_128bead, color='orange', alpha=0.65, s=22)
err8 = ax.errorbar(temps[0:4], vol_128bead, label="P=128", yerr=sem_128bead, capsize=2.0, fmt="o", color='orange', markersize=6, marker="x", linestyle=(0, (3, 1, 1, 1, 1, 1)))
ax.set_xlabel('Temperature (K)', fontsize=14)
ax.set_ylabel('Volume (Å$^{3}$)', fontsize=14)
ax.set_ylim(182.25, 184.75)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
ax.legend(handles=[err8, err7, err6, err5, err4, err3, err2, err1], loc="upper center", fontsize=14, ncols=4, bbox_to_anchor=(0.5, 1.2), framealpha=1)
ax.grid(True)

# inset Axes....
x1, x2, y1, y2 = 90, 510, 184.575, 184.725  # subregion of the original image
axins2 = ax.inset_axes(
    [0.4, 0.05, 0.57, 0.37],
    xlim=(x1, x2), ylim=(y1, y2))
axins2.scatter(temps, vol_1bead, color='green', alpha=0.65, s=22)
err1 = axins2.errorbar(temps, vol_1bead, label="P=1", yerr=sem_1bead, capsize=2.0, fmt="o", color='green', markersize=6, marker="o", linestyle="solid")
axins2.scatter(temps, vol_2bead, color='#ba9500', alpha=0.65, s=22)
err2 = axins2.errorbar(temps, vol_2bead, label="P=2", yerr=sem_2bead, capsize=2.0, fmt="o", color='#ba9500', markersize=6, marker="v", linestyle="dotted")
axins2.scatter(temps, vol_4bead, color='#2dad76', alpha=0.65, s=22)
err3 = axins2.errorbar(temps, vol_4bead, label="P=4", yerr=sem_4bead, capsize=2.0, fmt="o", color='#2dad76', markersize=6, marker="d", linestyle="dashed")
axins2.scatter(temps, vol_8bead, color='blue', alpha=0.65, s=22)
err4 = axins2.errorbar(temps, vol_8bead, label="P=8", yerr=sem_8bead, capsize=2.0, fmt="o", color='blue', markersize=6, marker="s", linestyle="dashdot")
axins2.scatter(temps, vol_16bead, color='#00439c', alpha=0.65, s=22)
err5 = axins2.errorbar(temps, vol_16bead, label="P=16", yerr=sem_16bead, capsize=2.0, fmt="o", color='#00439c', markersize=6, marker="P", linestyle=(0, (5, 1)))
axins2.scatter(temps, vol_32bead, color='purple', alpha=0.65, s=22)
err6 = axins2.errorbar(temps, vol_32bead, label="P=32", yerr=sem_32bead, capsize=2.0, fmt="o", color='purple', markersize=6, marker="*", linestyle=(5, (10, 3)))
axins2.scatter(temps[0:6], vol_64bead, color='#520202', alpha=0.65, s=22)
err7 = axins2.errorbar(temps[0:6], vol_64bead, label="P=64", yerr=sem_64bead, capsize=2.0, fmt="o", color='#520202', markersize=6, marker="p", linestyle=(0, (3, 1, 1, 1)))
axins2.scatter(temps[0:4], vol_128bead, color='orange', alpha=0.65, s=22)
err8 = axins2.errorbar(temps[0:4], vol_128bead, label="P=128", yerr=sem_128bead, capsize=2.0, fmt="o", color='orange', markersize=6, marker="x", linestyle=(0, (3, 1, 1, 1, 1, 1)))
axins2.set_xlim(90, 510)
axins2.set_ylim(184.575, 184.725)
axins2.set_xticks([100, 200, 300, 400, 500])
axins2.set_yticks([184.600, 184.650, 184.700])
axins2.tick_params(axis='both', labelsize=11, which='both', bottom=True, left=True, zorder=True)

plt.savefig('myfig.png', dpi=300, transparent=True)
plt.show()
