import os

def parse_knapsack_instance(filename):
    # Initialize lists for profits and weights
    profits = []
    weights = []

    # Read the file and parse the contents
    with open(filename, 'r') as file:
        # Read the first line which contains `n` and `wmax`
        first_line = file.readline().strip()
        n, wmax = map(int, first_line.split())

        # Read subsequent lines for items' profit and weight
        for line in file:
            if line.strip():  # Ensure line is not empty
                profit, weight = map(int, line.strip().split())
                profits.append(profit)
                weights.append(weight)

    if len(profits) != n or len(weights) != n:
        raise ValueError("The number of items does not match the number specified in the file")

    return n, wmax, profits, weights

