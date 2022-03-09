from typing import Any, Type
import numpy


class Function_Generic():
    '''Abstract generic class'''
    return_type = None
    x_type = None

    def get_return_type(self) -> Type:
        return self.return_type
    
    def get_value(self, x: Any) -> Any:
        pass

    def get_gradient_value(self, x: Any) -> Any:
        pass

    def get_gradient_square_value(self, x: Any) -> Any:
        pass

    def get_x_type(self) -> Type:
        return self.x_type


class Function_F(Function_Generic):
    '''Function F class'''

    return_type = float
    x_type = float

    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_value(self, x: float) -> float:
        # returns function value for given x
        result = self.a * x**3 + self.b * x**2 + self.c * x + self.d
        return result

    def get_gradient_value(self, x: float) -> float:
        result = 3 * self.a * x**2 + 2 * self.b * x + self.c
        return result

    def get_gradient_square_value(self, x: float) -> float:
        result = 6 * self.a * x + 2 * self.b
        return result


class Function_G(Function_Generic):
    '''Function G class'''

    return_type = float
    x_type = numpy.matrix

    def __init__(self,  a: numpy.matrix, b: numpy.matrix, c: float) -> None:
        self.c = c
        self.b = b
        self.a = a

    def get_value(self, x: numpy.matrix) -> float:
        # returns function value for given x
        result = self.c + self.b.transpose() * x + x.transpose() * self.a * x
        return numpy.asscalar(result)

    def get_gradient_value(self, x: numpy.matrix) -> numpy.matrix:
        result = self.b + self.a * x + self.a.transpose() * x # derivative calculated using matrixcalculus.org
        return result

    def get_gradient_square_value(self, x: numpy.matrix) -> numpy.matrix:
        result = self.a.transpose() + self.a # derivative calculated using matrixcalculus.org
        return result
