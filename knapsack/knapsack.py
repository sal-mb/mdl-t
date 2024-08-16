from mip import Model, xsum, maximize, BINARY, CBC

# Importing instace reader for the problem
from reader import parse_knapsack_instance

import argparse
import os

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Parse a 0/1 Knapsack problem instance from a file.")
    parser.add_argument('filename', type=str, help="Name of the knapsack problem instance file")

    args = parser.parse_args()
    filename = args.filename

    # Parse the knapsack instance (c_1 and c_2 are the challenge variables)
    try:
        n, wmax, profits, weights, c_1, c_2 = parse_knapsack_instance(filename)
        print(f"Number of items: {n}")
        print(f"Knapsack capacity: {wmax}")
        print(f"Profits: {profits}")
        print(f"Weights: {weights}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # --------------------------------- model ---------------------------
    I = range(n)

    m = Model(solver_name=CBC)
    m.verbose = 0

    # ----------------------- decision variables ------------------------
    x = [m.add_var(var_type=BINARY) for i in I]
    
    # --------------------- add your variables below --------------------



    # ------------------------ objective function -----------------------
    m.objective = maximize(xsum(profits[i] * x[i] for i in I))

 
    # -------------------------- constraints ----------------------------
    m += xsum(weights[i] * x[i] for i in I) <= wmax
    

    # ------------------- add your constraints below --------------------
    
    m += x[c_2] <= x[c_1]


    # --------------------------- solving -------------------------------
    m.optimize(max_nodes_same_incumbent=50000,max_seconds_same_incumbent=60)
    

    # ------------------------ printing results -------------------------
    selected = [i for i in I if x[i].x >= 0.99]

    print("selected items: {}".format(selected))

    print("objective value: ", m.objective_value)

if __name__ == "__main__":
    main()
