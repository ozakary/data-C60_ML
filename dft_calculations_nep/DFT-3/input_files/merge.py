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

