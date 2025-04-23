import os
import pandas as pd

# Loop over the ${i} folders (from 0 to 31)
for i in range(32):
    i_folder = f"./{i}"
    i_index = f"{i}"
    # List to store dataframes from each ${j} folder
    dataframes = []
    
    # Loop over the ${j} folders (from 1 to 5)
    for j in range(1, 6):
        csv_file = f"{i_folder}/{j}/sigma_iso_new_predictions_with_structures.csv"
        
        # Check if the file exists before loading
        if os.path.exists(csv_file):
            print(f"Loading {csv_file}")
            df = pd.read_csv(csv_file)
            dataframes.append(df)
        else:
            print(f"File {csv_file} not found.")

    # Concatenate all dataframes vertically
    if dataframes:
        concatenated_df = pd.concat(dataframes, axis=0, ignore_index=True)
        
        # Save the concatenated dataframe in the ${i} folder
        output_file = f"{i_folder}/predicted_sigma_iso_beads_{i_index}.csv"
        concatenated_df.to_csv(output_file, index=False)
        print(f"Saved concatenated file to {output_file}")
    else:
        print(f"No valid CSV files found in {i_folder}")

