import time
from typing import Any, Union

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
    def calculate_minimum(function: Function_Generic,
                          x: Union[float, numpy.matrix],
                          break_condition: int,
                          break_condition_value: Any) -> float:
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
        return x, function.get_value(x)

class NewtonMethod(CalculationMethod):

    @staticmethod
    def calculate_minimum(function: Function_Generic,
                          x: Union[float, numpy.matrix],
                          break_condition: int,
                          break_condition_value: Any) -> float:
        i = 0
        start_time = time.time()
        while True:
            if function.get_x_type() == float:
                inverse_of_square_gradient = 1 / function.get_gradient_square_value(x)
            else:
                inverse_of_square_gradient = numpy.linalg.inv(function.get_gradient_square_value(x))
            # print("inverse of square", inverse_of_square_gradient)
            # print("gradient val", function.get_gradient_value(x))
            # print("x", x)
            # print("mult", inverse_of_square_gradient * function.get_gradient_value(x))
            x =  - inverse_of_square_gradient * function.get_gradient_value(x)
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
        return x, function.get_value(x)
