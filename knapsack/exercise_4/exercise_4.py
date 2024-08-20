from mip import Model, xsum, maximize, BINARY, CBC

def kp_exercise_4(data, sacks, solution):

    n = data['n']
    wmax = data['capacity']
    p = data['profits']
    w = data['weights']

    I = range(n)

    # set of knapsacks of exercise 4
    K = range(sacks)


    # ------------------------------ model ------------------------------
    m = Model(solver_name=CBC)
    m.verbose = 0


    # ----------------------- decision variables ------------------------
    x = [[m.add_var(var_type=BINARY) for k in K] for i in I]




    # ------------------------ objective function -----------------------
    


    # -------------------------- constraints ----------------------------




    # --------------------------- solving -------------------------------
    set_solution(solution, m, x, K)
    status = m.optimize(max_nodes_same_incumbent=50000,max_seconds_same_incumbent=60)

    return status.value



def set_solution(solution, m, x, K):

    for k in K:
        for i in range(len(x)):
            if i in solution[k]:
                m += x[i][k] == 1
            else:
                m += x[i][k] == 0

