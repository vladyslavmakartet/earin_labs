import equation, methods
import numpy


# split for F and G functions
# declare one dictionary and pass values depending on type
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
             print(f"Your choice is not in available {text} options. Available options {available_options}. Please try again!")
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
            print('ERROR: Input must be a {type_} value! Please try again!\n')
            continue
        break
    return number

def format_input(text, delimiter):
    text = text.replace(' ', '')
    text = text.split(delimiter)
    return text

def stopping_conditions(function_type: str):
    print(separation_line)
    print(f"""Please choose preferred stopping condition
          1. Maximum number of iterations
          2. Desired value {function_type} to reach
          3. Maximum computation time 
          """)
    choice = getNumericChoice("stopping condition", [1,2,3])
    if choice == 1:
        value = getNumericScalar("the value of the selected stopping condition", type_="int")
    else:
        value = getNumericScalar("the value of the selected stopping condition")
    return choice-1, value

def ui():
    choices = {"method": 0, "function": 0}
    print(chr(27) + "[2J") # clear output
    print(header_text)
    
    print("Please select method to use (Gradient: 1, Newton: 2): ")
    choices["method"] = getNumericChoice("method", [1,2])

    print("Please select function to use (F(x): 1, G(x): 2): ")
    # print(function_types)
    choices["function"] = getNumericChoice("function", [1,2])
    print(separation_line)
    
    try:
        if choices["function"] == 1:
            F_coeff = {}
            F_coeff["a"] = getNumericScalar("a")
            F_coeff["b"] = getNumericScalar("b")
            F_coeff["c"] = getNumericScalar("c")
            F_coeff["d"] = getNumericScalar("d")
            print(separation_line)
            
            print('Please define starting point (by scalar number - 1 | by uniform distribution - 2): ')
            choice = getNumericChoice("starting point", [1,2])
            
            # fix here
            if choice == 1:
                start_point = getNumericScalar("starting point")
            elif choice == 2:
                start_point = input('Please define range for uniform distribution (i.e.: 1,2): ')
                start_point = format_input(start_point, ',')
                start_point = numpy.asarray(start_point).astype(float)
            else:
                raise ValueError
            
            F_coeff["stop_cond_type"], F_coeff["stop_cond_value"] = stopping_conditions("F(x)")
            
            
    except ValueError:
        pass
if __name__ == "__main__": # for test only
    ui()

