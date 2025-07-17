import numpy as np
import os

writefilepath = "volumes_ell_average.txt"
beads = 32

# Calculates the average volume over the beads for every sample point

full_results = []
for i in range(beads):
    full_results.append(np.loadtxt('volumes_ell_' + str(i) + 'bead.txt', delimiter=';')[:,1])

with open(writefilepath, 'w') as f:
    for j in range(len(full_results[0])):
        vol = 0
        for i in range(beads):
            vol += full_results[i][j]
        f.write(str(vol/beads) + '\n')
        vol = 0

