from mip import Model, xsum, maximize, BINARY, CBC

def knapsack_solver(data, j, k, l, solution):

    n = data['n']
    wmax = data['capacity']
    profits = data['profits']
    weights = data['weights']

    I = range(n)


    # ------------------------------ model ------------------------------
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


    

    # --------------------------- solving -------------------------------
    set_solution(solution, m, x)
    status = m.optimize(max_nodes_same_incumbent=50000,max_seconds_same_incumbent=60)


    return status.value



def set_solution(solution, m, x):

    for i in range(len(x)):

        if i in solution:
            m += x[i] == 1
        else:
            m += x[i] == 0
