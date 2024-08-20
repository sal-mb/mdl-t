import itertools

from pathlib import Path

import sys 

# import exercise files
sys.path.insert(0, './exercise_1')
sys.path.insert(0, './exercise_2')
sys.path.insert(0, './exercise_3')
sys.path.insert(0, './exercise_4')

from exercise_1 import kp_exercise_1
from exercise_2 import kp_exercise_2
from exercise_3 import kp_exercise_3
from exercise_4 import kp_exercise_4

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
    
    file_path = "./exercise_" + str(exercise) + "/instance"
    file_path_check = "./exercise_" + str(exercise) + "/check"

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

def generate_partitions(n, m):
    numbers = list(range(0, n))
    
    def partitions(numbers, m):
        if m == 1:
            yield [numbers]
        else:
            for i in range(1, len(numbers)):
                for part in itertools.combinations(numbers, i):
                    remaining = [x for x in numbers if x not in part]
                    for subpartition in partitions(remaining, m-1):
                        yield [list(part)] + subpartition
    
    return list(partitions(numbers, m))

def exercise_solution(exercise, data, test):
    if exercise ==1:
        return kp_exercise_1(data, 0, 1, test)
    elif exercise == 2:
        return kp_exercise_2(data, 0, 1, test)
    elif exercise == 3:
        return kp_exercise_3(data, 0, 1, 2, test)
    else:
        return kp_exercise_4(data, 3, test)
