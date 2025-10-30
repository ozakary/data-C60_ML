import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def read_log_data(file_path):
    """Read training log data from CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully loaded {len(data)} records from {file_path}")
        return data
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return None

def plot_sigma_curves(log_data, property_name, ax):
    """Create a single plot with both MAE and RMSE decay curves using logarithmic scale."""
    print(f"Creating training curve plot for {property_name}...")
    
    # Extract relevant columns
    epochs = np.arange(1, len(log_data) + 1)  # Assuming each row is an epoch
    mae_col = f"MAE_{property_name}"
    rmse_col = f"RMSE_{property_name}"
    
    # Check if columns exist
    if mae_col not in log_data.columns or rmse_col not in log_data.columns:
        print(f"Error: {mae_col} or {rmse_col} column not found in log file")
        return
    
    # Extract values
    mae_values = log_data[mae_col].values
    rmse_values = log_data[rmse_col].values
    
    # Plot both curves
    ax.plot(epochs, mae_values, 'o-', color='orange', linewidth=2, markersize=4, label=r'$\sigma_{\text{iso}}$ MAE / ppm')
    ax.plot(epochs, rmse_values, 's-', color='purple', linewidth=2, markersize=4, label=r'$\sigma_{\text{iso}}$ RMSE / ppm')
    
    # Add legend
    ax.legend(fontsize=14)
    
    
def plot_training_curves(log_data, property_name, ax):
    """Create a single plot with both MAE and RMSE decay curves using logarithmic scale."""
    print(f"Creating training curve plot for {property_name}...")
    
    # Extract relevant columns
    epochs = np.arange(1, len(log_data) + 1)  # Assuming each row is an epoch
    train_col = f"Train {property_name}"
    val_col = f"Validation {property_name}"
    
    # Check if columns exist
    if train_col not in log_data.columns or val_col not in log_data.columns:
        print(f"Error: {train_col} or {val_col} column not found in log file")
        return
    
    # Extract values
    train_values = log_data[train_col].values
    val_values = log_data[val_col].values
    
    # Plot both curves
    ax.plot(epochs, train_values, 'o-', color='blue', linewidth=2, markersize=4, label='training loss')
    ax.plot(epochs, val_values, 's-', color='green', linewidth=2, markersize=4, label='validation loss')
    
    # Add legend
    ax.legend(fontsize=14)

def init_plot(ax):

    # Add labels and title
    ax.set_xlabel('Epoch', fontsize=18)
    ax.set_ylabel('Error / Loss', fontsize=18)

    # Format tick labels
    ax.tick_params(axis='both', which='major', labelsize=14, length=6, width=1)

    # Set y-axis to log scale
    ax.set_yscale('log')

    # Add grid for better readability with log scale
    ax.grid(True, which="both", ls="-", alpha=0.2)


def main():
    print("Starting training log plotting script...")
    
    # Define path to log file
    log_file = "./sigma_iso/log/log.csv"
    
    # Check if file exists
    if not os.path.exists(log_file):
        print(f"Error: Log file {log_file} not found.")
        return
    
    # Read log data
    log_data = read_log_data(log_file)
    if log_data is None:
        return

    # Prepare the plot
    plt.figure(figsize=(8, 6))
    ax = plt.gca()
    init_plot(ax)
    
    # Process the property (based on the log file structure)
    property_name = "sigma_iso"
    # Create plot
    plot_sigma_curves(log_data, property_name, ax)

    property_name = "loss"
    plot_training_curves(log_data, property_name, ax)

    # Save plot
    combined_filename = 'figure_S6.png'
    plt.savefig(combined_filename, dpi=300)
    print(f"Saved combined plot to {combined_filename}")
    plt.show()

    print("\nLog plotting completed successfully!")

if __name__ == "__main__":
    main()
