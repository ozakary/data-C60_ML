# This code produces an xyz file of empty C60 configuration with reference DFT energy and forces to be used in the training of NEP ML model.

import os

# Force conversion coefficient. The minus sign is here so NEP can read the forces correctly. See NEP documentation for details.
C = -51.42208619083232 # Ha/Bohr to eV/Å

path = os.getcwd()
xyzfile = path.split("/")[-1].replace("cluster", "coord") + ".xyz"

r = open("energy", "r")
lines = r.readlines()
energy = float(lines[1].strip().split(" ")[1])*27.2114079527 # Ha to eV
firstline = "energy={} config_type=nep3xyz Lattice=\"25.0 0.0 0.0 0.0 25.0 0.0 0.0 0.0 25.0\" Properties=species:S:1:pos:R:3:force:R:3\n".format(energy)
r.close()

g = open("gradient", "r")
gradlines = g.readlines()
g.close()

w = open("ref.xyz", "w")
w.write("60\n")
w.write(firstline)

def read_gradient(i):
    line = gradlines[62+i].strip().split(" ")
    gradient = [float(line[0].replace("D", "E"))*C, float(line[2].replace("D", "E"))*C, float(line[4].replace("D", "E"))*C]
    return " {} {} {}".format(gradient[0], gradient[1], gradient[2])

lines = open(xyzfile, "r")
for i, val in enumerate(lines.readlines()):
    if (i > 1):
        w.write(val.strip("\n") + str(read_gradient(i-2)) + "\n")
w.close()

