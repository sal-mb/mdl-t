from mip import Model, xsum, maximize, BINARY, CBC
import argparse
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

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Parse a 0/1 Knapsack problem instance from a file.")
    parser.add_argument('filename', type=str, help="Name of the knapsack problem instance file")

    args = parser.parse_args()
    filename = args.filename

    # Parse the knapsack instance
    try:
        n, wmax, profits, weights = parse_knapsack_instance(filename)
        print(f"Number of items: {n}")
        print(f"Knapsack capacity: {wmax}")
        print(f"Profits: {profits}")
        print(f"Weights: {weights}")
    except ValueError as e:
        print(f"Error: {e}")

    I = range(n)

    m = Model(solver_name=CBC)

    x = [m.add_var(var_type=BINARY) for i in I]

    m.objective = maximize(xsum(profits[i] * x[i] for i in I))

    m += xsum(weights[i] * x[i] for i in I) <= wmax

    m.optimize()

    selected = [i for i in I if x[i].x >= 0.99]
    print("selected items: {}".format(selected))

    print("objectivevalue: ", m.objective_value)

if __name__ == "__main__":
    main()
