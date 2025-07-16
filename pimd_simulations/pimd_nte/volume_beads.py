import ase.io as io
from ase import Atoms
import numpy as np
import math
import os

#This script reads a GPUMD PIMD trajectory file in xyz format, calculates and writes average volume over the beads of each step into a separate file
path = os.getcwd()
# Define the number of beads, change according to the bead number of the simulation
beads = 32

# Calculate the center of mass of a given configuration
def center_of_mass(coords):
    com = []
    for i in range(3):
        sum = 0
        for j in range(60):
            sum += coords[j][i]
        com.append(sum/60)
    return np.array(com)

# Calculate the gyration tensor
def gyrtensor(coords):
    com = center_of_mass(coords)
    gyrtensor = np.array([[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])
    for i in range(3):
        for j in range(3):
                for k in range(len(coords)):
                    gyrtensor[i][j] += (coords[k][i] - com[i])*(coords[k][j] - com[j])
                gyrtensor[i][j] /= 60
    return gyrtensor

# Calculate the volume of C60 from the gyration tensor treating the molecule as a sphere
def calcvolume_sphere(tensor):
    eigenvalues = np.linalg.eigvals(tensor)
    radius_gyr = (eigenvalues[0] + eigenvalues[1] + eigenvalues[2])**0.5
    volume = 4/3 * math.pi * radius_gyr**3
    return volume

# Calculates the volume of the fullerene by treating the molecule as an ellipsoid
def calcvolume_ell(tensor):
    eigenvalues = np.linalg.eigvals(tensor)
    volume = 4 * math.pi * 3**(1/2) * eigenvalues[0]**(1/2) * eigenvalues[1]**(1/2) * eigenvalues[2]**(1/2)
    return volume

# Main function: Loops through all the beads and calculates the volume of each configuration and writes results to a txt file
for i in range(beads):
    print('calculating volumes for bead ' + str(i))
    atomspath = path + "/beads_dump_" + str(i) + ".xyz"
    atoms = io.read(atomspath, index=':')

    writefilepath = path + "/volumes_ell_" + str(i) + "bead.txt"

    with open(writefilepath, 'a') as f:
        for k in range(len(atoms)) :
            molecule = atoms[k].get_positions()
            vol = calcvolume_ell(gyrtensor(molecule))
            f.write(str(k) + ';' + str(vol) + '\n')
