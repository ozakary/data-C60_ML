def split_xyz_file(input_file, output_prefix, structures_per_file=1001):
    """
    Splits an .xyz file containing multiple structures into smaller .xyz files.

    Parameters:
        input_file (str): Path to the input .xyz file.
        output_prefix (str): Prefix for the output .xyz files.
        structures_per_file (int): Number of structures per output file.
    """
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Initialize structure count and file index
    structure_count = 0
    file_index = 1
    structure_lines = []
    structure_data = []  # Temporary storage for a single structure

    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect the start of a new structure by '60'
        if line.strip() == '60':
            # Add the '60' line and the following lines to the current structure
            structure_data.append(line)  # Add the '60' line
            i += 1
            structure_data.append(lines[i])  # Add the 'Time' line
            i += 1
            # Add the next 60 lines for atomic positions
            for j in range(60):
                structure_data.append(lines[i])
                i += 1
            
            # Now we have one full structure, increment the structure count
            structure_count += 1

            # Append this structure to the output buffer
            structure_lines.extend(structure_data)
            structure_data = []  # Clear the structure data for the next structure

            # If the number of structures reaches the limit, write them to a file
            if structure_count % structures_per_file == 0:
                output_file = f"{output_prefix}_{file_index}.xyz"
                with open(output_file, 'w') as outfile:
                    outfile.writelines(structure_lines)
                print(f"Written {structures_per_file} structures to {output_file}")
                
                # Prepare for the next file
                structure_lines = []
                file_index += 1
        else:
            i += 1  # Continue to the next line if not in a '60' structure block

    # Write any remaining structures
    if structure_lines:
        output_file = f"{output_prefix}_{file_index}.xyz"
        with open(output_file, 'w') as outfile:
            outfile.writelines(structure_lines)
        print(f"Written remaining structures to {output_file}")

if __name__ == "__main__":
    input_file = "beads_dump_0.xyz"  # Replace with your actual .xyz file path
    output_prefix = "split_beads_dump_0"  # Replace with your desired output prefix
    split_xyz_file(input_file, output_prefix)

