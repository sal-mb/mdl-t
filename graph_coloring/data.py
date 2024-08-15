import os

def parse_graph_file(filename):
    with open(filename, 'r') as file:
        # Read the first line to get the number of lines (size of the matrix)
        num_lines = int(file.readline().strip())

        # Initialize an empty matrix
        matrix = []

        # Read each subsequent line and convert it to a list of integers
        for _ in range(num_lines):
            line = file.readline().strip()
            row = list(map(int, line.split()))
            matrix.append(row)

    return num_lines, matrix

