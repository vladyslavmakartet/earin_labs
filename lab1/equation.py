from typing import Type


class Function_Generic():
    type = None

    def get_return_type(self) -> Type:
        return self.type

class Function_F(Function_Generic):
    type = int

    def __init__(self, a: int, b: int, c: int, d: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_value(self, x: int) -> int:
        result = self.a * x**3 + self.b * x**2 + self.c * x + self.d
        return result
