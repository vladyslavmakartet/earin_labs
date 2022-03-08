from typing import Optional, Union

import numpy
from equation import Function_Generic

class CalculationMethod():

    @staticmethod
    def calculate_minimum() -> None:
        pass

class GradientDescent(CalculationMethod):

    @staticmethod
    def calculate_minimum(function: Function_Generic, x: Union[float, numpy.matrix], max_iterations: Optional[int] = None) -> float:
        beta = 0.2
        i = 0
        while True:
            x = x - beta * function.get_gradient_value(x)
            beta *= 0.6
            i += 1
            if max_iterations and i >= max_iterations:
                break
        return function.get_value(x)