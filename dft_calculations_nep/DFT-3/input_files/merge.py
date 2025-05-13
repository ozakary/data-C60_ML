# Assign an xyz-file (ref.xyz) containing an empty C60 structure with reference DFT data (E, F) to train or test dataset with 0.7 and 0.3 probabilities respectively.

import random

ft = open('../train.xyz', "a")
fv = open('../test.xyz', "a")
rand = random.random()
if (rand < 0.3):
    with open('ref.xyz') as fp:
        fv.write(fp.read())
else:
    with open('ref.xyz') as fp:
        ft.write(fp.read())
ft.close()
fv.close()

