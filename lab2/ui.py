from ui_common import getNumericScalar, format_input, is_symmetric, is_positive_definite, print_parameters
import numpy as np
import sys
import equation
import algorithm

header_text = '''
===============================================================================
#   Genetic algorithm for analysis of multidimensional quadratic function     #
===============================================================================
#   Authors: Grzegorczyk Patryk, Vladyslav Makartet                           #
===============================================================================
'''
separation_line = '===============================================================================\n'
yes = ['y', 'yes', 'Y', 'Yes']
# function_type = '''
# F(x) = c+(b^T)*x+(x^T)*A*x (c - scalar number, b - vector of n numbers, A - 𝑛 𝑥 𝑛 matrix, x - vector)
# '''


def ui():
    params = {}  # dict of all inputs
    print(chr(27) + "[2J")  # clear output
    print(header_text)
    while True:
        try:
            params["c"] = getNumericScalar("c")
            in_text = input('Please input vector B (i.e.: 1,2,3): ')
            vector_b = format_input(in_text, ',')
            vector_b = [[i] for i in vector_b]
            vector_len = len(vector_b)
            vector_b = np.asmatrix(vector_b).astype(
                float)
            vector_temp = []

            print('Please input symmetric matrix with dimension {n}x{n}'.format(
                n=vector_len) + ': ')
            for x in range(0, vector_len):
                in_text = input(
                    '= Please input {n}th row of matrix A (i.e.: 1,2,3): '.format(n=x))
                temp_text = format_input(in_text, ',')
                assert len(temp_text) == vector_len, (
                    f"Please input symmetric matrix with dimension {vector_len}x{vector_len}")
                vector_temp.append(temp_text)

            matrix_a = np.asmatrix(vector_temp).astype(
                float)
            if not (is_symmetric(matrix_a) and is_positive_definite(matrix_a)):
                raise ValueError

            params["b"] = vector_b
            params["a"] = matrix_a
            print("\n" + separation_line)

            params["d"] = getNumericScalar("d", "int")
            params["d"] += 1
            params["dimensionality"] = getNumericScalar(
                "dimensionality", "int")
            params["population_size"] = getNumericScalar(
                "population size", "int")
            params["crossover_proba"] = getNumericScalar(
                "crossover probability")
            params["mutation_proba"] = getNumericScalar("mutation probability")
            params["iter_num"] = getNumericScalar("number of iteration", "int")

        except AssertionError as e:
            print(f"ERROR: {e}\n")
            continue
        except ValueError as e:
            print(f"ERROR: {e}\n")
            continue
        except np.linalg.LinAlgError:
            print(
                'Defined matrix is not a positive-definite! Please input a valid one and try again!\n')
            continue
        break

    print(separation_line)
    print_parameters(params)
    run_program(params)

    ans = input('=   Would you like to input new variables (y | n): ')
    if ans in yes:
        ui()
    else:
        sys.exit()


def run_program(params: dict):
    print(separation_line)

    function_to_process = equation.Function_G(
        params["a"], params["b"], params["c"])
    last_population = algorithm.run_algorithm(params["dimensionality"],
                                              params["population_size"],
                                              params["d"],
                                              params["mutation_proba"],
                                              params["crossover_proba"],
                                              params["iter_num"],
                                              function_to_process)

    results = {}
    for i in range(len(last_population)):
        results[i] = function_to_process.get_value(last_population[i])
    print("Output population:")
    for key, value in results.items():
        # transposed for more compact output
        print(
            f"= Member #{key}: {last_population[key].transpose()}.\t Target function value: {value}")

    print("\nMAX of the function: ")
    print(
        f"= Member: {last_population[max(results, key=results.get)].transpose()}.\t Target function value: {results[max(results, key=results.get)]}")


if __name__ == "__main__":
    ui()
