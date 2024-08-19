from knapsack import knapsack_solver

from pathlib import Path

import sys

def get_args():

    if len(sys.argv) > 1:
        # Get all arguments after the script name
        return int(sys.argv[1])
    else:
        print("Missing parameters... \n python main.py [exercise number]")
        sys.exit(1)

def parse_check_file(file_path):

    check_values = []

    with open(file_path, 'r') as file:
        line = file.readline().strip()
        check_values = list(map(int, line.split()))

    return check_values


def parse_exercise_files(exercise):
    
    file_path = "./exercises/" + str(exercise) + "/instance"
    file_path_check = "./exercises/" + str(exercise) + "/check"

    n = 0
    capacity = 0
    profits = []
    weights = []
    n_tests = 0
    tests = []
    checks = parse_check_file(file_path_check)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Parse the sections based on the format
    n, capacity = map(int, lines[0].split())
    profits = list(map(int, lines[1].split()))
    weights = list(map(int, lines[2].split()))
    n_tests = int(lines[3])
    
    # Extract solutions
    solutions_start_index = 4
    tests = [list(map(int, line.split())) for line in lines[solutions_start_index:]]
    
    data = {
        'n': n,
        'capacity': capacity,
        'profits': profits,
        'weights': weights
    }
    return data, n_tests, tests, checks


def print_formatted_arrays(array, status):
    """
    Print an array formatted with a dotted line and a status message.
    
    :param array: The array to print.
    :param status: Status message to display.
    """
    # Convert array to string
    array_str = str(array)
    
    # Calculate lengths
    array_length = len(array_str)
    status_length = 1
    
    # Total width of the line
    total_width = max(array_length + status_length + 5, 50)  # Adjust total width as needed

    # Create the dotted line
    dotted_line = '.' * (total_width - array_length - status_length - 2)  # 2 for spaces around dots
    
    # Format the output line
    line = f"{array_str} {dotted_line}"
    

        # Print the line
    if status:
        print(line,"✅")
    else:
        print(line,"❌")


def exercise_solution(exercise, data, test):
    if exercise <= 2:
        return knapsack_solver(data, 0, 1, -1, test)
    else:
        return knapsack_solver(data, 0, 1, 2, test)