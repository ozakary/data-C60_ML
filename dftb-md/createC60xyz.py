import os

path = os.getcwd()
xyzfile = path.split("/")[-1].replace("cluster", "coord") + ".xyz"

w = open("temp.xyz", "w")

lines = open(xyzfile, "r")
for i, val in enumerate(lines.readlines()):
    if (i == 0):
        w.write(val.strip("\n").replace("61", "60") + "\n")
    if (i > 0 and i < 62):
        print(val)
        w.write(val.strip("\n") + "\n")
w.close()

