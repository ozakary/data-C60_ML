import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.metrics import mean_absolute_error, mean_squared_error

fig, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(2, 3, layout='none', figsize=(12, 7))

fig.subplots_adjust(left=0.105, right=0.968, wspace=0.274, top=0.955, bottom=0.098, hspace=0.33)


# Load the chemical shielding DFT results and the chemical shielding values predicted by SchNet NMR-ML model
sigma_train = pd.read_csv('model_sigma_predictions/sigma_train_data.csv')
sigma_val = pd.read_csv('model_sigma_predictions/sigma_val_data.csv')
sigma_test = pd.read_csv('model_sigma_predictions/sigma_test_data.csv')

sigma_train_target = sigma_train['Target']
sigma_train_pred = sigma_train['Prediction']

sigma_val_target = sigma_val['Target']
sigma_val_pred = sigma_val['Prediction']

sigma_test_target = sigma_test['Target']
sigma_test_pred = sigma_test['Prediction']

# Draw the histograms
plot1 = ax1.hist(sigma_train_target, 15, facecolor='blue', alpha=0.75, label="training")
ax1.set_xlabel(r'$\sigma_{\text{iso}}^{\text{DFT}}$ / ppm', fontsize=13)
ax1.set_ylabel('Count', fontsize=13)
ax1.tick_params(axis='x', labelsize=13)
ax1.tick_params(axis='y', labelsize=13)
ax1.legend(["training"], loc="upper left", fontsize=12, framealpha=1)


plot2 = ax2.hist(sigma_val_target, 15, facecolor='green', alpha=0.75, label="validation")
ax2.set_xlabel(r'$\sigma_{\text{iso}}^{\text{DFT}}$ / ppm', fontsize=13)
ax2.tick_params(axis='x', labelsize=13)
ax2.tick_params(axis='y', labelsize=13)
ax2.legend(["validation"], loc="upper left", fontsize=12, framealpha=1)


plot3 = ax3.hist(sigma_test_target, 15, facecolor='darkorange', alpha=0.75, label="testing")
ax3.set_xlabel(r'$\sigma_{\text{iso}}^{\text{DFT}}$ / ppm', fontsize=13)
ax3.tick_params(axis='x', labelsize=13)
ax3.tick_params(axis='y', labelsize=13)
ax3.legend(["testing"], loc="upper left", fontsize=12, framealpha=1)


# Calculate linear regression parameters
slope_train, intercept_train, r_value_train, p_value_train, std_err_train = stats.linregress(sigma_train_target, sigma_train_pred)
rmse_train = np.sqrt(mean_squared_error(sigma_train_target, sigma_train_pred))
mae_train = mean_absolute_error(sigma_train_target, sigma_train_pred)

slope_val, intercept_val, r_value_val, p_value_val, std_err_val = stats.linregress(sigma_val_target, sigma_val_pred)
r_squared_val = r_value_val**2
rmse_val = np.sqrt(mean_squared_error(sigma_val_target, sigma_val_pred))
mae_val = mean_absolute_error(sigma_val_target, sigma_val_pred)

slope_test, intercept_test, r_value_test, p_value_test, std_err_test = stats.linregress(sigma_test_target, sigma_test_pred)
r_squared_test = r_value_test**2
rmse_test = np.sqrt(mean_squared_error(sigma_test_target, sigma_test_pred))
mae_test = mean_absolute_error(sigma_test_target, sigma_test_pred)


# Draw the correlation plots
ax4.scatter(sigma_train_target, sigma_train_pred, marker = 'o', alpha=0.4, color='blue', label="training")
min_val = min(min(sigma_train_target)-20, min(sigma_train_pred)-20)
max_val = max(max(sigma_train_target)+20, max(sigma_train_pred)+20)
ax4.plot([min_val, max_val], [min_val, max_val], 'r-', alpha=0.8)
ax4.text(-17, 68, f'RMSE = {rmse_train:.2f}', fontsize=12)
ax4.text(-17, 60, f'MAE = {mae_train:.2f}', fontsize=12)
ax4.text(-17, 52, f'R$^2$ = {r_value_train**2:.4f}', fontsize=12)
ax4.tick_params(axis='x', labelsize=13)
ax4.tick_params(axis='y', labelsize=13)
ax4.legend(["training"], loc="lower right", fontsize=13, framealpha=1)
ax4.set_xlabel(r'$\sigma_{\text{iso}}^{\text{DFT}}$ / ppm', fontsize=13)
ax4.set_ylabel(r'$\sigma_{\text{iso}}^{\text{ML}}$ / ppm', fontsize=13)
ax4.set_xlim([-20, 75])
ax4.set_ylim([-20, 75])

ax5.scatter(sigma_val_target, sigma_val_pred, marker= 's', alpha=0.4, color='green', label="validation")
ax5.plot([min_val, max_val], [min_val, max_val], 'r-', alpha=0.8)
ax5.text(-17, 68, f'RMSE = {rmse_val:.2f}', fontsize=12)
ax5.text(-17, 60, f'MAE = {mae_val:.2f}', fontsize=12)
ax5.text(-17, 52, f'R$^2$ = {r_value_val**2:.4f}', fontsize=12)
ax5.tick_params(axis='x', labelsize=13)
ax5.tick_params(axis='y', labelsize=13)
ax5.legend(["validation"], loc="lower right", fontsize=13, framealpha=1)
ax5.set_xlabel(r'$\sigma_{\text{iso}}^{\text{DFT}}$ / ppm', fontsize=13)
ax5.set_xlim([-20, 75])
ax5.set_ylim([-20, 75])

ax6.scatter(sigma_test_target, sigma_test_pred, marker='x', alpha=0.4, color='darkorange', label="testing")
ax6.plot([min_val, max_val], [min_val, max_val], 'r-', alpha=0.8)
ax6.text(-17, 68, f'RMSE = {rmse_test:.2f}', fontsize=12)
ax6.text(-17, 60, f'MAE = {mae_test:.2f}', fontsize=12)
ax6.text(-17, 52, f'R$^2$ = {r_value_test**2:.4f}', fontsize=12)
ax6.tick_params(axis='x', labelsize=13)
ax6.tick_params(axis='y', labelsize=13)
ax6.legend(["testing"], loc="lower right", fontsize=13, framealpha=1)
ax6.set_xlabel(r'$\sigma_{\text{iso}}^{\text{DFT}}$ / ppm', fontsize=13)
ax6.set_xlim([-20, 75])
ax6.set_ylim([-20, 75])


plt.savefig('figure_5.png', dpi=300)
plt.show()
