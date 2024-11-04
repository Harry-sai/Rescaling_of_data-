import sys
import math
import random

file1 = sys.argv[1] #combined_ab.bed
file2 = sys.argv[2] #Pulling_no_line file
output_base_path = sys.argv[3]
num_files = int(sys.argv[4])

# Read second file into a dictionary
length_dict = {}
with open(file2, 'r') as f:
    for line in f:
        length, value = line.strip().split()
        length = int(length)
        value = math.ceil(float(value))  # Ceiling the value
        length_dict[length] = value

#shuffeling lines of combined file 
with open (file1, 'r') as file :
    lines = file.readlines()
   
for i in range(num_files) :
    output_path = f"{output_base_path}_{i + 1}.bed"
    count_dict = {k: 0 for k in length_dict}

    shuffled_lines = lines[:]
    random.shuffle(lines)
    
    with open (output_path,'w') as outputfile :
        for line in lines :
            cols = line.strip().split()
            length = int(cols[3])
            
            if length in length_dict and count_dict[length] < length_dict[length]:
                outputfile.write(line)
                count_dict[length] += 1
