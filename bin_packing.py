from mip import Model, xsum, maximize, minimize, BINARY, CBC
import argparse
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

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Parse a 0/1 Knapsack problem instance from a file.")
    parser.add_argument('filename', type=str, help="Name of the knapsack problem instance file")
    
    args = parser.parse_args()
    filename = args.filename
    
    # Parse the knapsack instance
    try:
        n_itens, capacity, weights = parse_b_p_instance(filename)
        print(f"Number of items: {n_itens}")
        print(f"Sack capacity: {capacity}")
        print(f"Weights: {weights}")
    except ValueError as e:
        print(f"Error: {e}")
    
    #--------------------------- modeling ----------------------------
    bags = range(n_itens)

    itens = range(n_itens)

    m = Model(solver_name=CBC)

    x = [[m.add_var(var_type=BINARY) for i in bags] for j in itens]

    y = [m.add_var(var_type=BINARY) for i in bags]

    m.objective = minimize(xsum(y[i] for i in bags))

    for j in itens:
        m += xsum(x[i][j] for i in bags) == 1

    for i in bags:
        m += xsum(weights[j] * x[i][j] for j in itens) <= capacity * y[i]

    m.optimize()

    print("sla: ",m.objective_value)

if __name__ == "__main__":
    main()
