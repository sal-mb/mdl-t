import os

def parse_b_p_instance(filename):
    # Initialize lists for profits and weights
    weights = []
    n_itens = capacity = 0

    # Read the file and parse the contents
    with open(filename, 'r') as file:
        lines = file.readlines()

        if len(lines) < 3:
            raise ValueError("The file does not contain enough lines.")

        # First line: number of items
        n_itens = int(lines[0].strip())

        # Second line: capacity
        capacity = int(lines[1].strip())

        # Remaining lines: weights
        weights = [int(line.strip()) for line in lines[2:]]

    # Check if the number of weights matches the number of items
    if len(weights) != n_itens:
        raise ValueError("The number of items does not match the number specified in the file")

    return n_itens, capacity, weights


