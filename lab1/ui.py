import equation
import methods
import numpy
from ui_common import getNumericChoice, getNumericScalar, format_input, stopping_conditions, start_point, is_symmetric, is_positive_definite, print_parameters

# To do:
# add try with another method
# add error message with quiestion if want to continue
# add batch
header_text = '''
===============================================================================
#   Gradient Descent method and Newton's method for function minimalization   #
===============================================================================
#   Authors: Grzegorczyk Patryk, Vladyslav Makartet                           #
===============================================================================
'''
separation_line = '===============================================================================\n'
# function_types = '''
# F(x) = a*x^3+b*x^2+c*x+d (a, b, c, d are scalar numbers)
# G(x) = c+(b^T)*x+(x^T)*A*x (c - scalar number, b - d-dimensional vector, A - positive-definite matrix)
# '''


def ui():
    params = {}  # dict of all inputs
    print(chr(27) + "[2J")  # clear output
    print(header_text)

    print("Please select method to use (Gradient: 1, Newton: 2): ")
    params["method"] = getNumericChoice("method", [1, 2])

    print("Please select function to use (F(x): 1, G(x): 2): ")
    # print(function_types)
    params["function_type"] = getNumericChoice("function", [1, 2])
    print(separation_line)

    if params["function_type"] == 1:
        F_function = {}
        F_function["a"] = getNumericScalar("a")
        F_function["b"] = getNumericScalar("b")
        F_function["c"] = getNumericScalar("c")
        F_function["d"] = getNumericScalar("d")
        print(separation_line)
        params["start_point"] = start_point(1)
        print(separation_line)
        params["stop_cond_type"], params["stop_cond_value"] = stopping_conditions(
            "F(x)")
        params["F_function"] = F_function
    if params["function_type"] == 2:
        G_function = {}
        G_function["c"] = getNumericScalar("c")
        while True:
            try:
                in_text = input('Please input vector B (i.e.: 1,2,3): ')
                vector_b = format_input(in_text, ',')
                vector_len = len(vector_b)
                vector_b = numpy.asarray(vector_b).astype(float)

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

                matrix_a = numpy.asarray(vector_temp).astype(float)

                if not (is_symmetric(matrix_a) and is_positive_definite(matrix_a)):
                    raise ValueError
                G_function["b"] = vector_b
                G_function["a"] = matrix_a
                print(separation_line)
                params["start_point"] = start_point(1)
                print(separation_line)
                params["stop_cond_type"], params["stop_cond_value"] = stopping_conditions(
                    "G(x)")
                params["G_function"] = G_function
            except AssertionError as e:
                print(f"ERROR: {e}\n")
                continue
            except ValueError as e:
                print(f"ERROR: {e}\n")
                continue
            except numpy.linalg.LinAlgError:
                print(
                    'Defined matrix is not a positive-definite! Please input a valid one and try again!\n')
                continue
            break

    print("Would you like to run the program in batch/restart mode (yes: 1, no: 0)")
    params["batch"] = getNumericChoice("batch/restart mode", [0, 1])
    if params["batch"] == 1:
        params["batch_number"] = getNumericScalar(
            "how many times to restart", type_="int", onlyPositive=True)
    print(separation_line)
    print_parameters(params)
    run_program(params)


def run_program(params: dict):
    print(separation_line)
    if params["function_type"] == 1:
        function_to_process = equation.Function_F(params["F_function"]["a"],
                                                  params["F_function"]["b"],
                                                  params["F_function"]["c"],
                                                  params["F_function"]["d"]
                                                  )
    if params["function_type"] == 2:
        function_to_process = equation.Function_G(params["G_function"]["a"],
                                                  params["G_function"]["b"],
                                                  params["G_function"]["c"])


if __name__ == "__main__":  # for test only
    ui()
