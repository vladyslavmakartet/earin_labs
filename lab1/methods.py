from typing import Optional, Union

import numpy
from equation import Function_Generic

class CalculationMethod():

    @staticmethod
    def calculate_minimum() -> float:
        pass

class GradientDescent(CalculationMethod):

    @staticmethod
    def calculate_minimum(function: Function_Generic, x: Union[float, numpy.matrix], max_iterations: Optional[int] = None) -> float:
        beta = 0.01
        i = 0
        while True:
            x = x - beta * function.get_gradient_value(x)
            i += 1
            if max_iterations and i >= max_iterations:
                break
        return function.get_value(x)

class NewtonMethod(CalculationMethod):

    @staticmethod
    def calculate_minimum(function: Function_Generic, x: Union[float, numpy.matrix], max_iterations: Optional[int] = None) -> float:
        pass