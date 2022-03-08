import time
from typing import Any, Optional, Union

import numpy
from equation import Function_Generic

BREAK_ITERATIONS = 0
BREAK_TIME = 1
BREAK_VALUE_TO_REACH = 2

class CalculationMethod():

    @staticmethod
    def calculate_minimum() -> float:
        pass

class GradientDescent(CalculationMethod):

    @staticmethod
    def calculate_minimum(function: Function_Generic, x: Union[float, numpy.matrix], break_condition: int, break_condition_value: Any) -> float:
        beta = 0.01
        i = 0
        start_time = time.time()
        while True:
            x = x - beta * function.get_gradient_value(x)
            if break_condition == BREAK_ITERATIONS:
                i += 1
                if i >= break_condition_value:
                    break
            elif break_condition == BREAK_TIME:
                delta_time = time.time() - start_time
                if delta_time > break_condition_value:
                    break
            elif break_condition == BREAK_VALUE_TO_REACH:
                current_value = function.get_value(x)
                if current_value <= break_condition_value:
                    break
        return function.get_value(x)

class NewtonMethod(CalculationMethod):

    @staticmethod
    def calculate_minimum(function: Function_Generic, x: Union[float, numpy.matrix], break_condition: int, break_condition_value: Any) -> float:
        pass