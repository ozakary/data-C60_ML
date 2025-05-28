import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.metrics import mean_absolute_error, mean_squared_error

fig, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(2, 3, layout='none', figsize=(12, 7))

fig.subplots_adjust(left=0.105, right=0.968, wspace=0.274, top=0.955, bottom=0.098, hspace=0.33)


# Load the chemical shielding DFT results
sigma_train = sigma_train = pd.read_csv('sigma_dft_data/sigma_train_data.csv')
sigma_val = pd.read_csv('sigma_dft_data/sigma_val_data.csv')
sigma_test = pd.read_csv('sigma_dft_data/sigma_test_data.csv')

sigma_train_target = sigma_train['Target']
sigma_val_target = sigma_val['Target']
sigma_test_target = sigma_test['Target']

# Draw the histograms
plot1 = ax1.hist(sigma_train_target, 15, facecolor='blue', alpha=0.75, label="Train")
ax1.set_xlabel(r'$\sigma_{iso}^{DFT}$ / ppm', fontsize=13)
ax1.set_ylabel('Number of datapoints', fontsize=13)
ax1.tick_params(axis='x', labelsize=13)
ax1.tick_params(axis='y', labelsize=13)
ax1.legend(["Train"], loc="upper left", fontsize=12, framealpha=1)


plot2 = ax2.hist(sigma_val_target, 15, facecolor='green', alpha=0.75, label="Validation")
ax2.set_xlabel(r'$\sigma_{iso}^{DFT}$ / ppm', fontsize=13)
ax2.tick_params(axis='x', labelsize=13)
ax2.tick_params(axis='y', labelsize=13)
ax2.legend(["Validation"], loc="upper left", fontsize=12, framealpha=1)


plot3 = ax3.hist(sigma_test_target, 15, facecolor='darkorange', alpha=0.75, label="Test")
ax3.set_xlabel(r'$\sigma_{iso}^{DFT}$ / ppm', fontsize=13)
ax3.tick_params(axis='x', labelsize=13)
ax3.tick_params(axis='y', labelsize=13)
ax3.legend(["Test"], loc="upper left", fontsize=12, framealpha=1)

# Read the chemical shielding values predicted by SchNet NMR-ML model
sigma_train = pd.read_csv('sigma_dft_data/sigma_train_data.csv')
sigma_val = pd.read_csv('sigma_dft_data/sigma_val_data.csv')
sigma_test = pd.read_csv('sigma_dft_data/sigma_test_data.csv')

sigma_train_target = sigma_train['Target']
sigma_train_pred = sigma_train['Prediction']

sigma_val_target = sigma_val['Target']
sigma_val_pred = sigma_val['Prediction']

sigma_test_target = sigma_test['Target']
sigma_test_pred = sigma_test['Prediction']

# Calculate linear regression parameters
slope_train, intercept_train, r_value_train, p_value_train, std_err_train = stats.linregress(sigma_train_target, sigma_train_pred)
rmse_train = np.sqrt(mean_squared_error(sigma_train_target, sigma_train_pred))

slope_val, intercept_val, r_value_val, p_value_val, std_err_val = stats.linregress(sigma_val_target, sigma_val_pred)
r_squared_val = r_value_val**2
rmse_val = np.sqrt(mean_squared_error(sigma_val_target, sigma_val_pred))

slope_test, intercept_test, r_value_test, p_value_test, std_err_test = stats.linregress(sigma_test_target, sigma_test_pred)
r_squared_test = r_value_test**2
rmse_test = np.sqrt(mean_squared_error(sigma_test_target, sigma_test_pred))


# Draw the correlation plots
ax4.scatter(sigma_train_target, sigma_train_pred, marker = 'o', alpha=0.4, color='blue', label="Train")
min_val = min(min(sigma_train_target)-20, min(sigma_train_pred)-20)
max_val = max(max(sigma_train_target)+20, max(sigma_train_pred)+20)
ax4.plot([min_val, max_val], [min_val, max_val], 'r-', alpha=0.8)
ax4.text(-18, 68, f'Train RMSE = {rmse_train:.3f}', fontsize=12)
ax4.text(-18, 62, f'Train R$^2$ = {r_value_train**2:.3f}', fontsize=12)
ax4.tick_params(axis='x', labelsize=13)
ax4.tick_params(axis='y', labelsize=13)
ax4.legend(["Train"], loc="lower right", fontsize=13, framealpha=1)
ax4.set_xlabel(r'$\sigma_{iso}^{DFT}$ / ppm', fontsize=13)
ax4.set_ylabel(r'$\sigma_{iso}^{ML}$ / ppm', fontsize=13)
ax4.set_xlim([-20, 75])
ax4.set_ylim([-20, 75])

ax5.scatter(sigma_val_target, sigma_val_pred, marker= 's', alpha=0.4, color='green', label="Validation")
ax5.plot([min_val, max_val], [min_val, max_val], 'r-', alpha=0.8)
ax5.text(-18, 68, f'Validation RMSE = {rmse_val:.3f}', fontsize=12)
ax5.text(-18, 62, f'Validation R$^2$ = {r_value_val**2:.3f}', fontsize=12)
ax5.tick_params(axis='x', labelsize=13)
ax5.tick_params(axis='y', labelsize=13)
ax5.legend(["Validation"], loc="lower right", fontsize=13, framealpha=1)
ax5.set_xlabel(r'$\sigma_{iso}^{DFT}$ / ppm', fontsize=13)
ax5.set_xlim([-20, 75])
ax5.set_ylim([-20, 75])

ax6.scatter(sigma_test_target, sigma_test_pred, marker='x', alpha=0.4, color='darkorange', label="Test")
ax6.plot([min_val, max_val], [min_val, max_val], 'r-', alpha=0.8)
ax6.text(-18, 68, f'Test RMSE = {rmse_test:.3f}', fontsize=12)
ax6.text(-18, 62, f'Test R$^2$ = {r_value_test**2:.3f}', fontsize=12)
ax6.tick_params(axis='x', labelsize=13)
ax6.tick_params(axis='y', labelsize=13)
ax6.legend(["Test"], loc="lower right", fontsize=13, framealpha=1)
ax6.set_xlabel(r'$\sigma_{iso}^{DFT}$ / ppm', fontsize=13)
ax6.set_xlim([-20, 75])
ax6.set_ylim([-20, 75])


plt.savefig('figure_4.png', dpi=300, transparent=True)
plt.show()
