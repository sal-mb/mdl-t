from reader import exercise_solution, print_formatted_arrays, parse_exercise_files, get_args, generate_partitions

import time

def write_text_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def main():
    
    exercise = get_args()
    
    # reading instances 
    data, n_tests, tests, checks = parse_exercise_files(exercise)

    # counter variable
    got_right = 0

    # partitions for exercise 4
    if exercise == 4:
        tests = generate_partitions(data['n'],3)
        n_tests = len(tests)


    # reading check file
    for i in range(n_tests):
        time.sleep(2.0/127)
        
        status = exercise_solution(exercise, data, tests[i])
        
        #write_text_to_file("4/check", str(status) + ' ')
        if status == checks[i]:
            got_right += 1
            print_formatted_arrays(tests[i], 1)

        else:
            print_formatted_arrays(tests[i], 0)

    
    if got_right == n_tests:
        print("\n\033[32mAll Tests Passed!! \n")

    else:
        print(f"\n\033[31mWrong Answer - {got_right}/{n_tests} tests passed.\n")

if __name__ == "__main__":
    main()


