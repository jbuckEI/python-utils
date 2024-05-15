'''
Take flat data like:
x,y,z,x,y,z etc
and make

x y z
x y z
x y z

convert a 1D array in row-major order into a 2D array with only 3 columns
you need to specify the number of rows based on the length of the 1D array 
and the number of columns

python flat-to-column.py input.csv output.csv 3

'''

import sys



import sys


def main(input_file, output_file, columns):
    # Read input file
    with open(input_file, 'r') as f:
        data = f.read().strip()

    # Split the data into individual values
    values = data.split(',')

    rows = len(values) // columns  # Calculate the number of rows based on the length of the array
    if len(values) % columns != 0:
        raise ValueError("Number of elements in the array is not divisible by the number of columns.")
    
    # Initialize an empty 2D array
    arr_2d = [[0] * columns for _ in range(rows)]
    
    # Fill the 2D array with values from the 1D array in row-major order
    k = 0
    for j in range(rows):
        for i in range(columns):
            arr_2d[j][i] = values[k]
            k += 1
            
    # Write the transposed values to a text file
    with open(output_file, 'w') as f:
        for row in arr_2d:
            f.write('\t'.join(map(str,row)) + '\n')  # Separate columns by tabs    

if __name__ == "__main__":
    args = sys.argv[1:]
    input_file = args[0]
    output_file = args[1]
    columns = int(args[2])
    main(input_file, output_file, columns)

