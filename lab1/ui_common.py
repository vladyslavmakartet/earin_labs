import numpy


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
                f"Your choice is not in available {text} options. Available options {available_options}. Please try again!\n")
            continue
        break
    return choice


def getNumericScalar(coef: str, type_="numeric", onlyPositive=False) -> float:
    while True:
        try:
            if type_ == "int":
                number = int(input(f'Please enter {coef} ({type_}): '))
                if onlyPositive and number < 0:
                    number = 0
                    print("Value must be positive. Your input was set to zero.\n")
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
          2. Maximum computation time in seconds
          3. Desired value {function_type} to reach
          """)
    choice = getNumericChoice("stopping condition", [1, 2, 3])
    if choice == 1:
        value = getNumericScalar(
            "the value of the selected stopping condition", type_="int")
    else:
        value = getNumericScalar(
            "the value of the selected stopping condition")
    return choice-1, value


def start_point(function_type: int, vector_size=None):
    if function_type == 1:
        print('Please define starting point (by scalar number - 1 | by uniform distribution - 2)')
        choice = getNumericChoice("starting point", [1, 2])
        if choice == 1:
            start_point = getNumericScalar("starting point")
    if function_type == 2:
        print('Please define starting point (by initial vector - 1 | by uniform distribution - 2)')
        choice = getNumericChoice("starting point", [1, 2])
        if choice == 1:
            while True:
                try:
                    in_text = input(
                        'Please input initial vector (i.e.: 1,2,3): ')
                    start_point = format_input(in_text, ',')
                    start_point = [[i] for i in start_point]
                    start_point = numpy.asmatrix(start_point).astype(float)
                    if (start_point.size != vector_size):
                        raise ValueError(
                            "Initial vector size is incorrect! Please try again!\n")
                except ValueError as e:
                    print(f'ERROR: {e}\n')
                    continue
                break
    if choice == 2:
        while True:
            try:
                start_point = input(
                    'Please define range for uniform distribution (i.e.: 1,2) ([low, high]): ')
                start_point = format_input(start_point, ',')
                if all(isinstance(e, (int, float)) for e in start_point) and len(start_point) == 2:
                    if vector_size == None:
                        start_point = numpy.asarray(start_point).astype(float)
                        if int(start_point[0]) >= int(start_point[1]):
                            raise ValueError
                        else:
                            start_point = numpy.random.uniform(int(start_point[0]), int(
                                start_point[1]))  # case with F(x) func for 1 point

                    else:
                        if int(start_point[0]) >= int(start_point[1]):
                            raise ValueError
                        else:
                            start_point = numpy.random.uniform(int(start_point[0]), int(
                                start_point[1]), vector_size)  # case with G(x) func for size of vector points
                            start_point = numpy.asmatrix(
                                [[i] for i in start_point])
                else:
                    raise ValueError
            except ValueError:
                print(
                    'ERROR: Only two numeric numbers in ([low, high]) order allowed! Low cannot be >= High. Please try again!\n')
                continue
            break
    return start_point


def is_symmetric(A):
    return A.transpose().all() == A.all()


def is_positive_definite(A):
    numpy.linalg.cholesky(A)
    return True


def ask_for_batch():
    print("Would you like to run the program in batch/restart mode (yes: 1, no: 0)")
    batch = getNumericChoice("batch/restart mode", [0, 1])
    batch_number = 0
    if batch == 1:
        batch_number = getNumericScalar(
            "how many times to restart", type_="int", onlyPositive=True)
    return batch, batch_number


def print_parameters(params: dict):
    func_type = "F(x)" if params['function_type'] == 1 else "G(x)"
    method = "Gradient Descent" if params['method'] == 1 else "Newton's method"
    if params['function_type'] == 1:
        text_with_variables = f"""    scalar a: {params['F_function']['a']}
        scalar b: {params['F_function']['b']}
        scalar c: {params['F_function']['c']}
        scalar d: {params['F_function']['d']}"""
    else:
        text_with_variables = f"""    scalar c: {params['G_function']['c']}
        vector b: {params['G_function']['b']}
        matrix A:\n {params['G_function']['a']}"""
    batch = f"With restarting {params['batch_number']} times" if params['batch'] == 1 else "Without restarting"

    print(f"""You selected the following:
    = Method to use: {method}
    = Function of type: {func_type}
    = Defined variables:
    {text_with_variables}
    = Starting point: {params['start_point']}
    = Stop condition type: {params['stop_cond_type']}
    = Stop condition value: {params['stop_cond_value']}
    = {batch}
    """)
    input("Press Enter to continue...")
