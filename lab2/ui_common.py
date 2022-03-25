import numpy as np


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


def is_symmetric(A):
    return A.transpose().all() == A.all()


def is_positive_definite(A):
    np.linalg.cholesky(A)
    return True


def print_parameters(params: dict):
    text_with_variables = f"""    scalar c: {params['c']}
        vector b: {params['b']}
        matrix A:\n {params['a']}
        int d: {params["d"]-1}
        problem dimensionality: {params["dimensionality"]}
        population size: {params["population_size"]}
        crossover probability: {params["crossover_proba"]}
        mutation probability: {params["mutation_proba"]}
        number of iterations: {params["iter_num"]}"""

    print(f"""You entered the following:
= Defined variables:
    {text_with_variables}""")
    input("Press Enter to continue...")
