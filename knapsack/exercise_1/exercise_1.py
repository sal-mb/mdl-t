from mip import Model, xsum, maximize, BINARY, CBC

def kp_exercise_1(data, j, k, solution):

    n = data['n']
    wmax = data['capacity']
    p = data['profits']
    w = data['weights']

    I = range(n)


    # ------------------------------ model ------------------------------
    m = Model(solver_name=CBC)
    m.verbose = 0


    # ----------------------- decision variables ------------------------
    x = [m.add_var(var_type=BINARY) for i in I]
    




    # ------------------------ objective function -----------------------
    m.objective = maximize(xsum(p[i] * x[i] for i in I))

 
    # -------------------------- constraints ----------------------------
    m += xsum(w[i] * x[i] for i in I) <= wmax
    


    

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


