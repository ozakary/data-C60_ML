import os
import re
import csv
import pandas as pd

def extract_shielding_tensors(mpshift_path, structure_id):
    with open(mpshift_path, 'r') as file:
        lines = file.readlines()

    tensor_data = []
    molecule_name = f'empty_fullerene_{structure_id}'

    in_shielding_section = False
    atom_index = -1

    line_iterator = iter(lines)
    for line in line_iterator:
        if ">>>>> DFT MAGNETIC SHIELDINGS <<<<<" in line:
            in_shielding_section = True
            continue

        if in_shielding_section:
            if line.startswith("ATOM"):
                parts = line.split()
                atom_index += 1  # Increment atom_index to start from 0
            elif "total magnetic shielding:" in line:
                tensor = []
                # Skip to the tensor lines
                next(line_iterator)  # Skip "Tensor :" line
                next(line_iterator)  # Skip one empty line or header line if present

                for _ in range(3):
                    tensor_line = next(line_iterator).strip()
                    tensor_row = [float(x) for x in tensor_line.split()]
                    tensor.append(tensor_row)

                # Flatten the tensor and reorder to match the header format
                flat_tensor = [
                    tensor[0][0], tensor[1][0], tensor[2][0],
                    tensor[0][1], tensor[1][1], tensor[2][1],
                    tensor[0][2], tensor[1][2], tensor[2][2]
                ]
                tensor_data.append([molecule_name, atom_index] + flat_tensor)

    columns = ["molecule_name", "atom_index", "XX", "YX", "ZX", "XY", "YY", "ZY", "XZ", "YZ", "ZZ"]
    df = pd.DataFrame(tensor_data, columns=columns)
    return df

def extract_atomic_coordinates(xyz_path, structure_id):
    coordinates = []
    with open(xyz_path, 'r') as file:
        lines = file.readlines()

    atom_index = 0
    molecule_name = f'empty_fullerene_{structure_id}'

    for i in range(len(lines)):
        if i == 0 or (lines[i].strip() == '60' and i + 2 < len(lines)):  # Start processing after '60'
            i += 2  # Skip '60' and 'Time' lines
            for j in range(60):  # Read the next 60 lines
                atom_data = lines[i + j].split()
                atom = atom_data[0]
                x, y, z = atom_data[1:4]
                coordinates.append([molecule_name, atom_index, atom, float(x), float(y), float(z)])
                atom_index += 1
            break  # Assuming only one structure in the .xyz file

    return coordinates

def write_tensors_to_csv(output_path, tensors):
    tensors.to_csv(output_path, index=False)

def write_coordinates_to_csv(output_path, coordinates):
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['molecule_name', 'atom_index', 'atom', 'x', 'y', 'z'])
        csvwriter.writerows(coordinates)

def main():
    output_dir_tensors = 'dataset_schnet_shielding_tensors'
    output_dir_coordinates = 'dataset_schnet_atomic_coordinates'
    os.makedirs(output_dir_tensors, exist_ok=True)
    os.makedirs(output_dir_coordinates, exist_ok=True)

    all_tensors = []
    all_coordinates = []
    train_data = []

    cluster_folders = sorted([folder for folder in os.listdir() if folder.startswith('cluster_') and os.path.isdir(folder)], key=lambda x: int(re.findall(r'\d+', x)[0]))
    total_clusters = len(cluster_folders)

    for idx, folder in enumerate(cluster_folders):
        print(f'Processing folder {idx + 1} of {total_clusters}: {folder}')
        structure_id = re.findall(r'\d+', folder)[0]

        mpshift_path = os.path.join(folder, 'mpshift.out')
        if os.path.exists(mpshift_path):
            tensors = extract_shielding_tensors(mpshift_path, structure_id)

            # Read coordinates from coord_<ID>.xyz file
            xyz_path = os.path.join(folder, f'coord_{structure_id}.xyz')
            coordinates = extract_atomic_coordinates(xyz_path, structure_id)

            output_path_tensors = os.path.join(output_dir_tensors, f'empty_fullerene_{structure_id}.csv')
            output_path_coordinates = os.path.join(output_dir_coordinates, f'empty_fullerene_{structure_id}.csv')

            write_tensors_to_csv(output_path_tensors, tensors)
            write_coordinates_to_csv(output_path_coordinates, coordinates)

            all_tensors.append(tensors)
            all_coordinates.extend(coordinates)

            for i in range(len(coordinates)):
                train_data.append([len(train_data), f'empty_fullerene_{structure_id}'])
        else:
            print(f'Warning: mpshift.out not found in {folder}')

    # Write the concatenated output for tensors
    final_output_path_tensors = os.path.join(output_dir_tensors, 'magnetic_shielding_tensors.csv')
    print('Writing concatenated output for magnetic shielding tensors to magnetic_shielding_tensors.csv')
    if all_tensors:
        concatenated_tensors = pd.concat(all_tensors, ignore_index=True)
        concatenated_tensors.to_csv(final_output_path_tensors, index=False)

    # Write the concatenated output for coordinates
    final_output_path_coordinates = os.path.join(output_dir_coordinates, 'structures.csv')
    print('Writing concatenated output for atomic coordinates to structures.csv')
    write_coordinates_to_csv(final_output_path_coordinates, all_coordinates)

    # Write the train.csv file
    train_output_path = 'train.csv'
    print('Writing train.csv')
    with open(train_output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['id', 'molecule_name'])
        csvwriter.writerows(train_data)

    print('Processing complete!')

if __name__ == "__main__":
    main()

