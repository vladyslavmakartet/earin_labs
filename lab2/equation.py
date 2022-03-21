import numpy


class Function_G:
    '''Function G class'''

    def __init__(self,  a: numpy.matrix, b: numpy.matrix, c: float) -> None:
        self.c = c
        self.b = b
        self.a = a

    def get_value(self, x: numpy.matrix) -> float:
        # returns function value for given x
        result = self.c + self.b.transpose() * x + x.transpose() * self.a * x
        return numpy.asscalar(result)
