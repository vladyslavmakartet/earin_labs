import equation
import methods
import numpy


# add printing of variables
# add try with another method
# add error message with quiestion if want to continue
# split code into separate files
header_text = '''
===============================================================================
#   Gradient Descent method and Newton's method for function minimalization   #
===============================================================================
#   Authors: Grzegorczyk Patryk, Vladyslav Makartet                           #
===============================================================================
'''
separation_line = '==============================================================================='
# function_types = '''
# F(x) = a*x^3+b*x^2+c*x+d (a, b, c, d are scalar numbers)
# G(x) = c+(b^T)*x+(x^T)*A*x (c - scalar number, b - d-dimensional vector, A - positive-definite matrix)
# '''


def getNumericChoice(text: str, available_options: list) -> int:
    while True:
        try:
            choice = int(input('Enter your choice: '))
            assert choice in available_options
        except ValueError:
            print('ERROR: Input must be an integer! Please try again!\n')
            continue
        except AssertionError:
            print(
                f"Your choice is not in available {text} options. Available options {available_options}. Please try again!")
            continue
        break
    return choice


def getNumericScalar(coef: str, type_="numeric") -> float:
    while True:
        try:
            if type_ == "int":
                number = int(input(f'Please enter {coef} ({type_}): '))
            else:
                number = float(input(f'Please enter {coef} ({type_}): '))

        except ValueError:
            print(f'ERROR: Input must be a {type_} value! Please try again!\n')
            continue
        break
    return number



def format_input(text, delimiter) -> list:
    text = text.replace(' ', '')
    text = text.split(delimiter)
    text = [float(i) for i in text]
    return text


def stopping_conditions(function_type: str):
    print(f"""Please choose preferred stopping condition
          1. Maximum number of iterations
          2. Desired value {function_type} to reach
          3. Maximum computation time 
          """)
    choice = getNumericChoice("stopping condition", [1, 2, 3])
    if choice == 1:
        value = getNumericScalar(
            "the value of the selected stopping condition", type_="int")
    else:
        value = getNumericScalar(
            "the value of the selected stopping condition")
    return choice-1, value


def start_point(function_type: int):
    if function_type == 1:
        print('Please define starting point (by scalar number - 1 | by uniform distribution - 2)')
        choice = getNumericChoice("starting point", [1, 2])

        if choice == 1:
            start_point = getNumericScalar("starting point")
        elif choice == 2:
            while True:
                try:
                    start_point = input(
                        'Please define range for uniform distribution (i.e.: 1,2): ')
                    start_point = format_input(start_point, ',')
                    if all(isinstance(e, (int, float)) for e in start_point) and len(start_point) == 2:
                        start_point = numpy.asarray(start_point).astype(float)
                    else:
                        raise ValueError
                except ValueError:
                    print(
                        'ERROR: Only two numeric numbers allowed! Please try again!\n')
                    continue
                break
    if function_type == 2:
        pass  # to do
    return start_point


def is_symmetric(A):
    return A.transpose().all() == A.all()

def is_positive_definite(A):
    numpy.linalg.cholesky(A)
    return True


def run_program(params: dict):
    pass


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
        F_function["start_point"] = start_point(1)
        print(separation_line)
        F_function["stop_cond_type"], F_function["stop_cond_value"] = stopping_conditions(
            "F(x)")
        params["F_function"] = F_function
    if params["function_type"] == 2:
        G_function = {}
        G_function["c"] = getNumericScalar("c")
        while True:
            try:
                print(separation_line)
                in_text = input('Please input vector B (i.e.: 1,2,3): ')
                vector_b = format_input(in_text, ',')
                vector_len = len(vector_b)
                vector_b = numpy.asarray(vector_b).astype(float)
                
                vector_temp = []

                print('Please input symmetric matrix with dimension {n}x{n}'.format(n=vector_len) + ': ')
                for x in range(0, vector_len):
                    in_text = input('= Please input {n}th row of matrix A (i.e.: 1,2,3): '.format(n=x))
                    temp_text = format_input(in_text, ',')
                    assert len(temp_text) == vector_len, (f"Please input symmetric matrix with dimension {vector_len}x{vector_len}")
                    vector_temp.append(temp_text)

                matrix_a = numpy.asarray(vector_temp).astype(float)

                if not (is_symmetric(matrix_a) and is_positive_definite(matrix_a)):
                    raise ValueError
                G_function["b"] = vector_b
                G_function["a"] = matrix_a
                params["G_function"] = G_function
            except AssertionError as e:
                print(f"ERROR: {e}")
                continue
            except ValueError as e:
                print(f"ERROR: {e}")
                continue
            except numpy.linalg.LinAlgError:
                print('Defined matrix is not a positive-definite! Please input a valid one and try again!')
                continue
            break

    print("Would you like to run the program in batch/restart mode (yes: 1, no: 0)")
    params["batch"] = getNumericChoice("batch/restart mode", [0, 1])

    run_program(params)


if __name__ == "__main__":  # for test only
    ui()
