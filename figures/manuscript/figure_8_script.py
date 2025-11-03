import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Load data of simulation in folder f and split the data at interval s
def ld(f,):
    return np.concatenate(np.loadtxt(f)[:], axis=None)

#Calculate mean and stdev and standard error
def calc_stats(data):
    means = []
    devs = []
    sems = []
    for el in data:
        means.append(np.round(np.mean(el), 4))
        devs.append(np.round(np.std(el), 4))
        sems.append(np.round(np.std(el)/(len(el))**(1/2), 4))
    return means, devs, sems


# Load the results
sig_hh = [ld('./260/hh/sigma.txt'),
        ld('./280/hh/sigma.txt'),
        ld('./300/hh/sigma.txt'),
        ld('./320/hh/sigma.txt'),
        ld('./340/hh/sigma.txt'),
        ]

sig_hp = [ld('./260/hp/sigma.txt'),
        ld('./280/hp/sigma.txt'),
        ld('./300/hp/sigma.txt'),
        ld('./320/hp/sigma.txt'),
        ld('./340/hp/sigma.txt'),
        ]

sig_single = [ld('./260/single/sigma.txt'),
        ld('./280/single/sigma.txt'),
        ld('./300/single/sigma.txt'),
        ld('./320/single/sigma.txt'),
        ld('./340/single/sigma.txt'),
        ]

# Calculate some stats
mean_hh, dev_hh, sem_hh = calc_stats(sig_hh)
mean_hp, dev_hp, sem_hp = calc_stats(sig_hp)
mean_single, dev_single, sem_single = calc_stats(sig_single)


# Print some data
print('260K hh: avg sigma iso = ' + str(mean_hh[0]) + ' and std = ' + str(dev_hh[0]) + ' and SEM: ' + str(sem_hh[0]) + " data: " + str(len(sig_hh[0])))
print('280K hh: avg sigma iso = ' + str(mean_hh[1]) + ' and std = ' + str(dev_hh[1]) + ' and SEM: ' + str(sem_hh[1]) + " data: " + str(len(sig_hh[1])))
print('300K hh: avg sigma iso = ' + str(mean_hh[2]) + ' and std = ' + str(dev_hh[2]) + ' and SEM: ' + str(sem_hh[2]) + " data: " + str(len(sig_hh[2])))
print('320K hh: avg sigma iso = ' + str(mean_hh[3]) + ' and std = ' + str(dev_hh[3]) + ' and SEM: ' + str(sem_hh[3]) + " data: " + str(len(sig_hh[3])))
print('340K hh: avg sigma iso = ' + str(mean_hh[4]) + ' and std = ' + str(dev_hh[4]) + ' and SEM: ' + str(sem_hh[4]) + " data: " + str(len(sig_hh[4])))
print("\n")
print('260K hp: avg sigma iso = ' + str(mean_hp[0]) + ' and std = ' + str(dev_hp[0]) + ' and SEM: ' + str(sem_hp[0]) + " data: " + str(len(sig_hp[0])))
print('280K hp: avg sigma iso = ' + str(mean_hp[1]) + ' and std = ' + str(dev_hp[1]) + ' and SEM: ' + str(sem_hp[1]) + " data: " + str(len(sig_hp[1])))
print('300K hp: avg sigma iso = ' + str(mean_hp[2]) + ' and std = ' + str(dev_hp[2]) + ' and SEM: ' + str(sem_hp[2]) + " data: " + str(len(sig_hp[2])))
print('320K hp: avg sigma iso = ' + str(mean_hp[3]) + ' and std = ' + str(dev_hp[3]) + ' and SEM: ' + str(sem_hp[3]) + " data: " + str(len(sig_hp[3])))
print('340K hp: avg sigma iso = ' + str(mean_hp[4]) + ' and std = ' + str(dev_hp[4]) + ' and SEM: ' + str(sem_hp[4]) + " data: " + str(len(sig_hp[4])))
print("\n")
print('260K single: avg sigma iso = ' + str(mean_single[0]) + ' and std = ' + str(dev_single[0]) + ' and SEM: ' + str(sem_single[0]) + " data: " + str(len(sig_single[0])))
print('280K single: avg sigma iso = ' + str(mean_single[1]) + ' and std = ' + str(dev_single[1]) + ' and SEM: ' + str(sem_single[1]) + " data: " + str(len(sig_single[1])))
print('300K single: avg sigma iso = ' + str(mean_single[2]) + ' and std = ' + str(dev_single[2]) + ' and SEM: ' + str(sem_single[2]) + " data: " + str(len(sig_single[2])))
print('320K single: avg sigma iso = ' + str(mean_single[3]) + ' and std = ' + str(dev_single[3]) + ' and SEM: ' + str(sem_single[3]) + " data: " + str(len(sig_single[3])))
print('340K single: avg sigma iso = ' + str(mean_single[4]) + ' and std = ' + str(dev_single[4]) + ' and SEM: ' + str(sem_single[4]) + " data: " + str(len(sig_single[4])))
print("\n")

#x-axis
temps = np.array([260, 280, 300, 320, 340])

# Linear fits
linreg_params_s = stats.linregress(temps, mean_single)
linreg_params_hh = stats.linregress(temps, mean_hh)
linreg_params_hp = stats.linregress(temps, mean_hp)

# Plot the data
fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(left=0.157, right=0.938, top=0.921, bottom=0.107)

single = ax.errorbar([260, 280, 300, 320, 340], mean_single, yerr=sem_single, capsize=2.0, marker="o", markersize=10, color='black', alpha=0.8, linestyle='')
ax.plot(temps, linreg_params_s.slope*temps + linreg_params_s.intercept, 'black', alpha=0.8, label='single', linestyle="solid")
print("Lin fit of single: " + str(np.round(linreg_params_s.slope, 6)) + "T" + " + " + str(np.round(linreg_params_s.intercept, 6)))
print(f'single slope gradient std error: {linreg_params_s.stderr*1000:.4f} ppb \n')
print(f'single slope intercept std error: {linreg_params_s.intercept_stderr*1000:.4f} ppb \n')

hh = ax.errorbar([260, 280, 300, 320, 340], mean_hh, yerr=sem_hh, capsize=2.0, marker="v", markersize=10, color='blue', alpha=0.8, linestyle='')
ax.plot(temps, linreg_params_hh.slope*temps + linreg_params_hh.intercept, 'blue', alpha=0.8, label='hh', linestyle="dotted")
print("Lin fit of hh: " + str(np.round(linreg_params_hh.slope, 6)) + "T" + " + " + str(np.round(linreg_params_hh.intercept, 6)))
print(f'hh slope gradient std error: {linreg_params_hh.stderr*1000:.4f} ppb \n')
print(f'hh slope intercept std error: {linreg_params_hh.intercept_stderr*1000:.4f} ppb \n')

hp = ax.errorbar([260, 280, 300, 320, 340], mean_hp, yerr=sem_hp, capsize=2.0, marker="d", markersize=10, color='orange', alpha=0.8, linestyle='')
ax.plot(temps, linreg_params_hp.slope*temps + linreg_params_hp.intercept, 'orange', alpha=0.8, label='hp', linestyle="dashed")
print("Lin fit of hp: " + str(np.round(linreg_params_hp.slope, 6)) + "T" + " + " + str(np.round(linreg_params_hp.intercept, 6)))
print(f'hp slope gradient std error: {linreg_params_hp.stderr*1000:.4f} ppb \n')
print(f'hp slope intercept std error: {linreg_params_hp.intercept_stderr*1000:.4f} ppb \n')

print(f'Grad(s) - Grad(hh) =  {(linreg_params_s.slope - linreg_params_hh.slope)*1000:.4f} ppb +- {(linreg_params_s.stderr**2+linreg_params_s.stderr**2)**(1/2)*1000:.4f} ppb')
print(f'Grad(s) - Grad(hp) =  {(linreg_params_s.slope - linreg_params_hp.slope)*1000:.4f} ppb +- {(linreg_params_s.stderr**2+linreg_params_s.stderr**2)**(1/2)*1000:.4f} ppb')

ax.set_ylabel(r'$\langle {\sigma}_{\text{iso}} \rangle$ (ppm)', fontsize=16)
ax.set_xlabel('$T$ (K)', fontsize=16)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
handles, labels = ax.get_legend_handles_labels()
ax.legend([single, hh, hp], ["$_{ }^{13}\\text{C}^{\\text{HHP}}_{1}$" + f': R$^2$ = {linreg_params_s.rvalue**2:.3f}', "$_{ }^{13}\\text{C}^{\\text{HH}}_{2}$" + f' : R$^2$ = {linreg_params_hh.rvalue**2:.3f}', "$_{ }^{13}\\text{C}^{\\text{HP}}_{2}$" + f' : R$^2$ = {linreg_params_hp.rvalue**2:.3f}'], loc="lower left", fontsize=16)
ax.grid(True)
plt.savefig('figure_8.png', dpi=300)
plt.show()
