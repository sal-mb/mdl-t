from mip import Model, xsum, maximize, minimize, BINARY, CBC

# Importing instace reader for the problem
from reader import parse_b_p_instance

import argparse
import os

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Parse a Bin Packing problem instance from a file.")
    parser.add_argument('filename', type=str, help="Name of the Bin Packing problem instance file")

    args = parser.parse_args()
    filename = args.filename

    # Parse the Bin Packing instance
    try:
        n_itens, capacity, weights = parse_b_p_instance(filename)
        print(f"Number of items: {n_itens}")
        print(f"Sack capacity: {capacity}")
        print(f"Weights: {weights}")
    except ValueError as e:
        print(f"Error: {e}")

    #--------------------------- model ----------------------------
    bins = range(n_itens)

    itens = range(n_itens)

    m = Model(solver_name=CBC)
    m.verbose = 0

    # --------------------- decision variables ----------------------
    x = [[m.add_var(var_type=BINARY) for i in bins] for j in itens]

    y = [m.add_var(var_type=BINARY) for i in bins]

    
    # ------------------ objective function ----------------
    m.objective = minimize(xsum(y[i] for i in bins))
    

    # ---------------------- constraints -------------------------
    for j in itens:
        m += xsum(x[i][j] for i in bins) == 1

    for i in bins:
        m += xsum(weights[j] * x[i][j] for j in itens) <= capacity * y[i]


    # ---------------------- solving ----------------------------
    m.optimize(max_nodes_same_incumbent=50000,max_seconds_same_incumbent=60)

    
    # -------------------- printing results ----------------------
    print("Bins used: ",m.objective_value, "\n")

    for i in bins:
        if y[i].x >= 0.99:
            item = [j for j in itens if x[i][j].x >= 0.99]
            print("itens in bin {}: {}".format(i,item))

if __name__ == "__main__":
    main()
