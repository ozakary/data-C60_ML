def convert_xyz_to_csv(input_file, output_file, start_id=100000, id_increment=400):
    """
    Converts the structures from the .xyz file to the desired CSV format.

    Parameters:
        input_file (str): Path to the input .xyz file (containing 1000 structures).
        output_file (str): Path to the output CSV file.
        start_id (int): Starting ID for the first structure.
        id_increment (int): Increment for the ID of each structure.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Write the header of the CSV file
        outfile.write("molecule_name,atom_index,atom,x,y,z\n")

        structure_id = start_id  # Initialize the first structure ID
        atom_index = 0           # Initialize the atom index

        lines = infile.readlines()
        i = 0
        
        while i < len(lines):
            # Detect the start of a structure by the '60' line
            if lines[i].strip() == '60':
                molecule_name = f"empty_fullerene_{structure_id}"
                atom_index = 0   # Reset atom index for each new structure
                i += 2  # Skip '60' and 'Time' lines

                # Process the next 60 lines of atomic positions
                for j in range(60):
                    atom_data = lines[i].split()  # Split the line into components
                    atom = atom_data[0]           # Atom symbol (e.g., 'C')
                    x, y, z = atom_data[1:4]      # x, y, z coordinates
                    outfile.write(f"{molecule_name},{atom_index},{atom},{x},{y},{z}\n")
                    atom_index += 1
                    i += 1

                # Increment the structure ID by the specified amount
                structure_id += id_increment
            else:
                i += 1  # Continue to the next line if not at the start of a structure

if __name__ == "__main__":
    # Example usage
    input_file = "split_beads_dump_0_1.xyz"  # Replace with the path to the .xyz file
    output_file = "converted_split_beads_dump_0_1.csv"  # Replace with the desired output .csv file path
    convert_xyz_to_csv(input_file, output_file)
