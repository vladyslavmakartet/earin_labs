import equation
import numpy
import sys
from ui_common import getNumericChoice, getNumericScalar, format_input, stopping_conditions, start_point, is_symmetric, is_positive_definite, print_parameters, ask_for_batch
from methods import NewtonMethod, GradientDescent

header_text = '''
===============================================================================
#   Gradient Descent method and Newton's method for function minimalization   #
===============================================================================
#   Authors: Grzegorczyk Patryk, Vladyslav Makartet                           #
===============================================================================
'''
separation_line = '===============================================================================\n'
yes = ['y', 'yes', 'Y', 'Yes']
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
                vector_b = [[i] for i in vector_b]
                vector_len = len(vector_b)
                vector_b = numpy.asmatrix(vector_b).astype(
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

                matrix_a = numpy.asmatrix(vector_temp).astype(
                    float)

                if not (is_symmetric(matrix_a) and is_positive_definite(matrix_a)):
                    raise ValueError
                G_function["b"] = vector_b
                G_function["a"] = matrix_a
                print(separation_line)
                params["start_point"] = start_point(2, vector_b.size)
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

    params["batch"], params["batch_number"] = ask_for_batch()
    print(separation_line)
    print_parameters(params)
    run_program(params)

    ans = 'y'
    while ans in yes:
        print(separation_line)
        ans = input('=   Would you like to run another method (y | n):')
        if ans in yes:
            params["batch"], params["batch_number"] = ask_for_batch()
            print("Please select method to use (Gradient: 1, Newton: 2): ")
            params["method"] = getNumericChoice("method", [1, 2])
            print(separation_line)
            print_parameters(params)
            run_program(params)
            print(separation_line)
    ans = input('=   Would you like to input new variables (y | n):')
    if ans in yes:
        ui()
    else:
        sys.exit()


def run_program(params: dict):
    print(separation_line)
    if params["function_type"] == 1:
        function_to_process = equation.Function_F(
            params["F_function"]["a"], params["F_function"]["b"], params["F_function"]["c"], params["F_function"]["d"])
    if params["function_type"] == 2:
        function_to_process = equation.Function_G(
            params["G_function"]["a"], params["G_function"]["b"], params["G_function"]["c"])
    try:
        if params["batch"] == 1:
            found_xs = []
            found_func_values = []
            for _ in range(params["batch_number"]):
                if params["method"] == 1:  # grad
                    x, func_value = GradientDescent.calculate_minimum(function_to_process,
                                                                      params["start_point"], params["stop_cond_type"], params["stop_cond_value"])
                if params["method"] == 2:  # newton
                    x, func_value = NewtonMethod.calculate_minimum(function_to_process,
                                                                   params["start_point"], params["stop_cond_type"], params["stop_cond_value"])
                found_xs.append(x)
                found_func_values.append(func_value)
            print("=   Results of", params["batch_number"], "iterations.")
            print(
                f"=   Mean value: x = {numpy.mean(found_xs)}, function of x = {numpy.mean(found_func_values)}")  # fix for nonetype
            print(
                f"=   Standard deviation: x = {numpy.std(found_xs)}, function of x = {numpy.std(found_func_values)}")  # fix for nonetype
            print("=   Obtained solutions for each program execution:")
            for i in range(len(found_xs)):
                print(f"\nIteration #{i}: ")
                print(f"x = {found_xs[i]}")
                print(f"Function of x = {found_func_values[i]}")

        else:
            if params["method"] == 1:  # grad
                print(GradientDescent.calculate_minimum(function_to_process,
                                                        params["start_point"], params["stop_cond_type"], params["stop_cond_value"]))
            if params["method"] == 2:  # newton
                print(NewtonMethod.calculate_minimum(function_to_process,
                                                     params["start_point"], params["stop_cond_type"], params["stop_cond_value"]))
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(
            f"ERROR: {e}. This error may result due to overflow as calculations go to infinity. Please input correct values!")
