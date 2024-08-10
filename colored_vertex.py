from mip import Model, xsum, minimize, BINARY, CBC
import argparse
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

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Parse a graph instance from a file.")
    parser.add_argument('filename', type=str, help="Name of the graph instance file")

    args = parser.parse_args()
    filename = args.filename

    # Parse the graph instance
    try:
        n_vertices, edges = parse_graph_file(filename)
        print(f"Number of vertices: {n_vertices}")
        print(f"Edges: {edges}")
    except ValueError as e:
        print(f"Error: {e}")

    colors = range(n_vertices)

    vertices = range(n_vertices)

    #--------------------------- model ------------------------

    m = Model(solver_name=CBC)

    v = [[m.add_var(var_type=BINARY) for i in vertices] for k in colors]

    y = [m.add_var(var_type=BINARY) for k in colors]

    m.objective = minimize(xsum(y[k] for k in colors))

    for i in vertices:
        m += xsum(v[i][k] for k in colors) == 1

    for i in vertices:
        for j in vertices:
            for k in colors:
                if i != j:
                    m += edges[i][j] * (v[i][k] + v[j][k]) <= y[k]

    m.optimize()

    print("number of colors used", m.objective_value)

if __name__ == "__main__":
    main()
