from typing import Type
import numpy

class Function_Generic():
    return_type = None
    x_type = None

    def get_return_type(self) -> Type:
        return self.return_type
    
    def get_value(self) -> None:
        pass

    def get_x_type(self) -> Type:
        return self.x_type

class Function_F(Function_Generic):
    return_type = int
    x_type = int

    def __init__(self, a: int, b: int, c: int, d: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_value(self, x: int) -> int:
        result = self.a * x**3 + self.b * x**2 + self.c * x + self.d
        return result

class Function_G(Function_Generic):
    return_type = int
    x_type = numpy.matrix

    def __init__(self,  a: numpy.matrix, b: numpy.matrix, c: int) -> None:
        self.c = c
        self.b = b
        self.a = a

    def get_value(self, x: numpy.matrix) -> int:
        b_part = self.b.transpose() * x
        a_part = x.transpose() * self.a * x
        result = self.c + b_part + a_part
        return numpy.asscalar(result)
