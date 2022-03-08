from typing import Type
import numpy

class Function_Generic():
    '''Abstract generic class'''
    return_type = None
    x_type = None

    def get_return_type(self) -> Type:
        return self.return_type
    
    def get_value(self) -> None:
        pass

    def get_derivative_value(self) -> None:
        pass

    def get_x_type(self) -> Type:
        return self.x_type

class Function_F(Function_Generic):
    '''Function F class'''

    return_type = int
    x_type = int

    def __init__(self, a: int, b: int, c: int, d: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_value(self, x: int) -> int:
        # returns function value for given x
        result = self.a * x**3 + self.b * x**2 + self.c * x + self.d
        return result

    def get_derivative_value(self, x: int) -> int:
        result = 3 * self.a * x**2 + 2 * self.b * x + self.c
        return result

class Function_G(Function_Generic):
    '''Function G class'''

    return_type = int
    x_type = numpy.matrix

    def __init__(self,  a: numpy.matrix, b: numpy.matrix, c: int) -> None:
        self.c = c
        self.b = b
        self.a = a

    def get_value(self, x: numpy.matrix) -> int:
        # returns function value for given x
        result = self.c + self.b.transpose() * x + x.transpose() * self.a * x
        return numpy.asscalar(result)

    def get_derivative_value(self, x: numpy.matrix) -> numpy.matrix:
        result = self.b + self.a * x + self.a.transpose() * x # derivative calculated from matrixcalculus.org
        return result
