import os

C = -51.42208619083232 # Ha/Bohr to eV/Å

path = os.getcwd()
xyzfile = path.split("/")[-1].replace("cluster", "coord") + ".xyz"

w = open("ref.xyz", "w")
#w.write("60\n")
#w.write(firstline)


lines = open(xyzfile, "r")
for i, val in enumerate(lines.readlines()):
    if (i == 0):
        w.write(val.strip("\n").replace("61", "60") + "\n")
    if (i > 0 and i < 62):
        print(val)
        w.write(val.strip("\n") + "\n")
w.close()

