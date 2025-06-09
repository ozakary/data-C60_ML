import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the results
results260hh = np.loadtxt('./260/hh/sigma2.txt')
results280hh = np.loadtxt('./280/hh/sigma2.txt')
results300hh = np.loadtxt('./300/hh/sigma2.txt')
results320hh = np.loadtxt('./320/hh/sigma2.txt')
results340hh = np.loadtxt('./340/hh/sigma2.txt')

results260hp = np.loadtxt('./260/hp/sigma2.txt')
results280hp = np.loadtxt('./280/hp/sigma2.txt')
results300hp = np.loadtxt('./300/hp/sigma2.txt')
results320hp = np.loadtxt('./320/hp/sigma2.txt')
results340hp = np.loadtxt('./340/hp/sigma2.txt')

results260single = np.loadtxt('./260/single/sigma2.txt')
results280single = np.loadtxt('./280/single/sigma2.txt')
results300single = np.loadtxt('./300/single/sigma2.txt')
results320single = np.loadtxt('./320/single/sigma2.txt')
results340single = np.loadtxt('./340/single/sigma2.txt')

sig260hh = np.concatenate((results260hh), axis=None)
sig280hh = np.concatenate((results280hh), axis=None)
sig300hh = np.concatenate((results300hh), axis=None)
sig320hh = np.concatenate((results320hh), axis=None)
sig340hh = np.concatenate((results340hh), axis=None)

sig260hp = np.concatenate((results260hp), axis=None)
sig280hp = np.concatenate((results280hp), axis=None)
sig300hp = np.concatenate((results300hp), axis=None)
sig320hp = np.concatenate((results320hp), axis=None)
sig340hp = np.concatenate((results340hp), axis=None)

sig300single = np.concatenate((results300single), axis=None)
sig260single = np.concatenate((results260single), axis=None)
sig280single = np.concatenate((results280single), axis=None)
sig320single = np.concatenate((results320single), axis=None)
sig340single = np.concatenate((results340single), axis=None)

# Calculate some stats
mean260hh = np.round(np.mean(sig260hh), 4)
dev260hh = np.round(np.std(sig260hh), 4)
mean280hh = np.round(np.mean(sig280hh), 4)
dev280hh = np.round(np.std(sig280hh), 4)
mean300hh = np.round(np.mean(sig300hh), 4)
dev300hh = np.round(np.std(sig300hh), 4)
mean320hh = np.round(np.mean(sig320hh), 4)
dev320hh = np.round(np.std(sig320hh), 4)
mean340hh = np.round(np.mean(sig340hh), 4)
dev340hh = np.round(np.std(sig340hh), 4)

mean260hp = np.round(np.mean(sig260hp), 4)
dev260hp = np.round(np.std(sig260hp), 4)
mean280hp = np.round(np.mean(sig280hp), 4)
dev280hp = np.round(np.std(sig280hp), 4)
mean300hp = np.round(np.mean(sig300hp), 4)
dev300hp = np.round(np.std(sig300hp), 4)
mean320hp = np.round(np.mean(sig320hp), 4)
dev320hp = np.round(np.std(sig320hp), 4)
mean340hp = np.round(np.mean(sig340hp), 4)
dev340hp = np.round(np.std(sig340hp), 4)

mean300single = np.round(np.mean(sig300single), 4)
dev300single = np.round(np.std(sig300single), 4)
mean260single = np.round(np.mean(sig260single), 4)
dev260single = np.round(np.std(sig260single), 4)
mean280single = np.round(np.mean(sig280single), 4)
dev280single = np.round(np.std(sig280single), 4)
mean320single = np.round(np.mean(sig320single), 4)
dev320single = np.round(np.std(sig320single), 4)
mean340single = np.round(np.mean(sig340single), 4)
dev340single = np.round(np.std(sig340single), 4)

sem260hh = np.round(np.std(sig260hh)/(len(sig260hh))**(1/2), 4)
sem280hh = np.round(np.std(sig280hh)/(len(sig280hh))**(1/2), 4)
sem300hh = np.round(np.std(sig300hh)/(len(sig300hh))**(1/2), 4)
sem320hh = np.round(np.std(sig320hh)/(len(sig320hh))**(1/2), 4)
sem340hh = np.round(np.std(sig340hh)/(len(sig340hh))**(1/2), 4)

sem260hp = np.round(np.std(sig260hp)/(len(sig260hp))**(1/2), 4)
sem280hp = np.round(np.std(sig280hp)/(len(sig280hp))**(1/2), 4)
sem300hp = np.round(np.std(sig300hp)/(len(sig300hp))**(1/2), 4)
sem320hp = np.round(np.std(sig320hp)/(len(sig320hp))**(1/2), 4)
sem340hp = np.round(np.std(sig340hp)/(len(sig340hp))**(1/2), 4)

sem300single = np.round(np.std(sig300single)/(len(sig300single))**(1/2), 4)
sem260single = np.round(np.std(sig260single)/(len(sig260single))**(1/2), 4)
sem280single = np.round(np.std(sig280single)/(len(sig280single))**(1/2), 4)
sem320single = np.round(np.std(sig320single)/(len(sig320single))**(1/2), 4)
sem340single = np.round(np.std(sig340single)/(len(sig340single))**(1/2), 4)

# Print some data
print('260K hh: avg sigma iso = ' + str(mean260hh) + ' and std = ' + str(dev260hh) + ' and SEM: ' + str(sem260hh) + " data: " + str(len(sig260hh)))
print('280K hh: avg sigma iso = ' + str(mean280hh) + ' and std = ' + str(dev280hh) + ' and SEM: ' + str(sem280hh) + " data: " + str(len(sig280hh)))
print('300K hh: avg sigma iso = ' + str(mean300hh) + ' and std = ' + str(dev300hh) + ' and SEM: ' + str(sem300hh) + " data: " + str(len(sig300hh)))
print('320K hh: avg sigma iso = ' + str(mean320hh) + ' and std = ' + str(dev320hh) + ' and SEM: ' + str(sem320hh) + " data: " + str(len(sig320hh)))
print('340K hh: avg sigma iso = ' + str(mean340hh) + ' and std = ' + str(dev340hh) + ' and SEM: ' + str(sem340hh) + " data: " + str(len(sig340hh)))
print("\n")

#x-axis
temps = np.array([260, 280, 300, 320, 340])

# Linear fits
linreg_params_s = stats.linregress(temps, [mean260single, mean280single, mean300single, mean320single, mean340single])
linreg_params_hh = stats.linregress(temps, [mean260hh, mean280hh, mean300hh, mean320hh, mean340hh])
linreg_params_hp = stats.linregress(temps, [mean260hp, mean280hp, mean300hp, mean320hp, mean340hp])

# Plot the data
fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(left=0.157, right=0.938, top=0.921, bottom=0.107)

single = ax.errorbar([260, 280, 300, 320, 340], [mean260single, mean280single, mean300single, mean320single, mean340single], yerr=[sem260single, sem280single, sem300single, sem320single, sem340single], capsize=2.0, marker="o", markersize=10, color='black', alpha=0.8, linestyle='')
ax.plot(temps, linreg_params_s.slope*temps + linreg_params_s.intercept, 'black', alpha=0.8, label='single', linestyle="solid")
print("Lin fit of single: " + str(np.round(linreg_params_s.slope, 6)) + "T" + " + " + str(np.round(linreg_params_s.intercept, 6)))
print(f'single slope gradient std error: {linreg_params_s.stderr*1000:.4f} ppb \n')
print(f'single slope intercept std error: {linreg_params_s.intercept_stderr*1000:.4f} ppb \n')

hh = ax.errorbar([260, 280, 300, 320, 340], [mean260hh, mean280hh, mean300hh, mean320hh, mean340hh], yerr=[sem260hh, sem280hh, sem300hh, sem320hh, sem340hh], capsize=2.0, marker="v", markersize=10, color='blue', alpha=0.8, linestyle='')
ax.plot(temps, linreg_params_hh.slope*temps + linreg_params_hh.intercept, 'blue', alpha=0.8, label='hh', linestyle="dotted")
print("Lin fit of hh: " + str(np.round(linreg_params_hh.slope, 6)) + "T" + " + " + str(np.round(linreg_params_hh.intercept, 6)))
print(f'hh slope gradient std error: {linreg_params_hh.stderr*1000:.4f} ppb \n')
print(f'hh slope intercept std error: {linreg_params_hh.intercept_stderr*1000:.4f} ppb \n')

hp = ax.errorbar([260, 280, 300, 320, 340], [mean260hp, mean280hp, mean300hp, mean320hp, mean340hp], yerr=[sem260hp, sem280hp, sem300hp, sem320hh, sem340hp], capsize=2.0, marker="d", markersize=10, color='orange', alpha=0.8, linestyle='')
ax.plot(temps, linreg_params_hh.slope*temps + linreg_params_hh.intercept, 'orange', alpha=0.8, label='hp', linestyle="dashed")
print("Lin fit of hp: " + str(np.round(linreg_params_hp.slope, 6)) + "T" + " + " + str(np.round(linreg_params_hp.intercept, 6)))
print(f'hp slope gradient std error: {linreg_params_hp.stderr*1000:.4f} ppb \n')
print(f'hp slope intercept std error: {linreg_params_hp.intercept_stderr*1000:.4f} ppb \n')

print(f'Grad(s) - Grad(hh) =  {(linreg_params_s.slope - linreg_params_hh.slope)*1000:.4f} ppb +- {(linreg_params_s.stderr**2+linreg_params_s.stderr**2)**(1/2)*1000:.4f} ppb')
print(f'Grad(s) - Grad(hp) =  {(linreg_params_s.slope - linreg_params_hp.slope)*1000:.4f} ppb +- {(linreg_params_s.stderr**2+linreg_params_s.stderr**2)**(1/2)*1000:.4f} ppb')

ax.set_ylabel('$\\sigma$ (ppm)', fontsize=16)
ax.set_xlabel('Temperature (K)', fontsize=16)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
handles, labels = ax.get_legend_handles_labels()
ax.legend([single, hh, hp], ["$_{ }^{13}\\text{C}_{1}$" + f'        : R$^2$ = {linreg_params_s.rvalue**2:.4f}', "$_{ }^{13}\\text{C}_{2}$ (HH)" + f' : R$^2$ = {linreg_params_hh.rvalue**2:.4f}', "$_{ }^{13}\\text{C}_{2}$ (HP)" + f' : R$^2$ = {linreg_params_hp.rvalue**2:.4f}'], loc="lower left", fontsize=16, framealpha=1)
ax.grid(True)

plt.savefig('figure_8.png', dpi=300, transparent=True)
plt.show()