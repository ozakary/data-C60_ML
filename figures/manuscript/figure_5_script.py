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

# Calculate statistics for the data
vol_1bead, std_1bead, sem_1bead = calc_stats(volumes_1bead)
vol_2bead, std_2bead, sem_2bead = calc_stats(volumes_2bead)
vol_4bead, std_4bead, sem_4bead = calc_stats(volumes_4bead)
vol_8bead, std_8bead, sem_8bead = calc_stats(volumes_8bead)
vol_16bead, std_16bead, sem_16bead = calc_stats(volumes_16bead)
vol_32bead, std_32bead, sem_32bead = calc_stats(volumes_32bead)
vol_64bead, std_64bead, sem_64bead = calc_stats(volumes_64bead)
vol_128bead, std_128bead, sem_128bead = calc_stats(volumes_128bead)

# x-axis
beads = [1, 2, 4, 8, 16, 32, 64, 128]

# Chancging the data structure properly -> P is the x-axis now insted of T
vol_100 = [vol_1bead[0], vol_2bead[0], vol_4bead[0], vol_8bead[0], vol_16bead[0], vol_32bead[0], vol_64bead[0], vol_128bead[0]]
vol_150 = [vol_1bead[1], vol_2bead[1], vol_4bead[1], vol_8bead[1], vol_16bead[1], vol_32bead[1], vol_64bead[1], vol_128bead[1]]
vol_200 = [vol_1bead[2], vol_2bead[2], vol_4bead[2], vol_8bead[2], vol_16bead[2], vol_32bead[2], vol_64bead[2], vol_128bead[2]]
vol_250 = [vol_1bead[3], vol_2bead[3], vol_4bead[3], vol_8bead[3], vol_16bead[3], vol_32bead[3], vol_64bead[3], vol_128bead[3]]
vol_300 = [vol_1bead[4], vol_2bead[4], vol_4bead[4], vol_8bead[4], vol_16bead[4], vol_32bead[4], vol_64bead[4]]
vol_350 = [vol_1bead[5], vol_2bead[5], vol_4bead[5], vol_8bead[5], vol_16bead[5], vol_32bead[5], vol_64bead[5]]
vol_400 = [vol_1bead[6], vol_2bead[6], vol_4bead[6], vol_8bead[6], vol_16bead[6], vol_32bead[6]]
vol_500 = [vol_1bead[7], vol_2bead[7], vol_4bead[7], vol_8bead[7], vol_16bead[7], vol_32bead[7]]

sem_100 = [sem_1bead[0], sem_2bead[0], sem_4bead[0], sem_8bead[0], sem_16bead[0], sem_32bead[0], sem_64bead[0], sem_128bead[0]]
sem_150 = [sem_1bead[1], sem_2bead[1], sem_4bead[1], sem_8bead[1], sem_16bead[1], sem_32bead[1], sem_64bead[1], sem_128bead[1]]
sem_200 = [sem_1bead[2], sem_2bead[2], sem_4bead[2], sem_8bead[2], sem_16bead[2], sem_32bead[2], sem_64bead[2], sem_128bead[2]]
sem_250 = [sem_1bead[3], sem_2bead[3], sem_4bead[3], sem_8bead[3], sem_16bead[3], sem_32bead[3], sem_64bead[3], sem_128bead[3]]
sem_300 = [sem_1bead[4], sem_2bead[4], sem_4bead[4], sem_8bead[4], sem_16bead[4], sem_32bead[4], sem_64bead[4]]
sem_350 = [sem_1bead[5], sem_2bead[5], sem_4bead[5], sem_8bead[5], sem_16bead[5], sem_32bead[5], sem_64bead[5]]
sem_400 = [sem_1bead[6], sem_2bead[6], sem_4bead[6], sem_8bead[6], sem_16bead[6], sem_32bead[6]]
sem_500 = [sem_1bead[7], sem_2bead[7], sem_4bead[7], sem_8bead[7], sem_16bead[7], sem_32bead[7]]

#Plot the data

fig, ax = plt.subplots(figsize=(8, 7))
fig.subplots_adjust(left=0.144, right=0.943, wspace=0.533, top=0.843, bottom=0.099)

plt.rcParams.update({'font.size': 16})

ax.scatter(beads, vol_100, color='green', alpha=0.8, s=22)
ax.scatter(beads, vol_150, color='#ba9500', alpha=0.8, s=22)
ax.scatter(beads, vol_200, color='#2dad76', alpha=0.8, s=22)
ax.scatter(beads, vol_250, color='blue', alpha=0.8, s=22)
ax.scatter(beads[0:7], vol_300, color='#00439c', alpha=0.8, s=22)
ax.scatter(beads[0:7], vol_350, color='purple', alpha=0.8, s=22)
ax.scatter(beads[0:6], vol_400, color='#520202', alpha=0.8, s=22)
ax.scatter(beads[0:6], vol_500, color='orange', alpha=0.8, s=22)
err1_1 = ax.errorbar(beads, vol_100, yerr=sem_100, capsize=2.0, fmt="o", label="T=100 K", color='green', markersize=6, marker="o", linestyle="solid")
err2_1 = ax.errorbar(beads, vol_150, yerr=sem_150, capsize=2.0, fmt="o", label="T=150 K", color='#ba9500', markersize=6, marker="v", linestyle="dotted")
err3_1 = ax.errorbar(beads, vol_200, yerr=sem_200, capsize=2.0, fmt="o", label="T=200 K", color='#2dad76', markersize=6, marker="d", linestyle="dashed")
err4_1 = ax.errorbar(beads, vol_250, yerr=sem_250, capsize=2.0, fmt="o", label="T=250 K", color='blue', markersize=6, marker="s", linestyle="dashdot")
err5_1 = ax.errorbar(beads[0:7], vol_300, yerr=sem_300, capsize=2.0, fmt="o", label="T=300 K", color='#00439c', markersize=6, marker="P", linestyle=(0, (5, 1)))
err6_1 = ax.errorbar(beads[0:7], vol_350, yerr=sem_350, capsize=2.0, fmt="o", label="T=350 K", color='purple', markersize=6, marker="*", linestyle=(5, (10, 3)))
err7_1 = ax.errorbar(beads[0:6], vol_400, yerr=sem_400, capsize=2.0, fmt="o", label="T=400 K", color='#520202', markersize=6, marker="p", linestyle=(0, (3, 1, 1, 1)))
err8_1 = ax.errorbar(beads[0:6], vol_500, yerr=sem_500, capsize=2.0, fmt="o", label="T=500 K", color='orange', markersize=6, marker="x", linestyle=(0, (3, 1, 1, 1, 1, 1)))
ax.legend(handles=[err8_1, err7_1, err6_1, err5_1, err4_1, err3_1, err2_1, err1_1], loc="upper center", fontsize=14, ncols=4, bbox_to_anchor=(0.5 , 1.2), framealpha=1)
ax.set_xlabel('Number of beads', fontsize=14)
ax.set_ylabel('Volume (Å$^{3}$)', fontsize=14)
ax.set_xscale('log', base=2)
ax.set_ylim(183, 184.8)
ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 128])
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
ax.grid(True)

# inset Axes
x1_1, x2_1, y1_1, y2_1 = 2, 135, 184.5, 184.725  # subregion of the original image
axins1 = ax.inset_axes(
    [0.5, 0.05, 0.47, 0.45],
    xlim=(x1_1, x2_1), ylim=(y1_1, y2_1))
axins1.set_xscale('log', base=2)
axins1.scatter(beads, vol_100, color='green', alpha=0.8, s=22)
axins1.scatter(beads, vol_150, color='#ba9500', alpha=0.8, s=22)
axins1.scatter(beads, vol_200, color='#2dad76', alpha=0.8, s=22)
axins1.scatter(beads, vol_250, color='blue', alpha=0.8, s=22)
axins1.scatter(beads[0:7], vol_300, color='#00439c', alpha=0.8, s=22)
axins1.scatter(beads[0:7], vol_350, color='purple', alpha=0.8, s=22)
axins1.scatter(beads[0:6], vol_400, color='#520202', alpha=0.8, s=22)
axins1.scatter(beads[0:6], vol_500, color='orange', alpha=0.8, s=22)
axins1.errorbar(beads, vol_100, yerr=sem_100, capsize=2.0, fmt="o", label="T=100 K", color='green', markersize=6, marker="o", linestyle="solid")
axins1.errorbar(beads, vol_150, yerr=sem_150, capsize=2.0, fmt="o", label="T=150 K", color='#ba9500', markersize=6, marker="v", linestyle="dotted")
axins1.errorbar(beads, vol_200, yerr=sem_200, capsize=2.0, fmt="o", label="T=200 K", color='#2dad76', markersize=6, marker="d", linestyle="dashed")
axins1.errorbar(beads, vol_250, yerr=sem_250, capsize=2.0, fmt="o", label="T=250 K", color='blue', markersize=6, marker="s", linestyle="dashdot")
axins1.errorbar(beads[0:7], vol_300, yerr=sem_300, capsize=2.0, fmt="o", label="T=300 K", color='#00439c', markersize=6, marker="P", linestyle=(0, (5, 1)))
axins1.errorbar(beads[0:7], vol_350, yerr=sem_350, capsize=2.0, fmt="o", label="T=350 K", color='purple', markersize=6, marker="*", linestyle=(5, (10, 3)))
axins1.errorbar(beads[0:6], vol_400, yerr=sem_400, capsize=2.0, fmt="o", label="T=400 K", color='#520202', markersize=6, marker="p", linestyle=(0, (3, 1, 1, 1)))
axins1.errorbar(beads[0:6], vol_500, yerr=sem_500, capsize=2.0, fmt="o", label="T=500 K", color='orange', markersize=6, marker="x", linestyle=(0, (3, 1, 1, 1, 1, 1)))

axins1.set_xticks([2, 4, 8, 16, 32, 64, 128])
axins1.tick_params(axis='both', labelsize=11, which='both', bottom=True, left=True, zorder=True)

plt.savefig('myfig.png', dpi=300, transparent=True)
plt.show()
