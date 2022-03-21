

from numpy import binary_repr

LIMIT_D = 8

class BinaryVectorOverflow(Exception):
    pass

class BinaryVector:

    def __init__(self, value: int, width_limit: int = LIMIT_D) -> None:
        if value.bit_length() + 1 > width_limit:
            raise BinaryVectorOverflow("Representation of a number requires too many bits")
        self.value = value
        self.width_limit = width_limit

    def __str__(self) -> str:
        return binary_repr(self.value, self.width_limit)

    def from_string(self, x: str) -> "BinaryVector":
        value = int(x, base=2)
        if value.bit_length() + 1 > self.width_limit:
            value = -int(x[1:], 2)
        return BinaryVector(value, width_limit=self.width_limit)

    def crossover(self, x: "BinaryVector", crossover_point: int) -> "BinaryVector":
        a = str(self)
        b = str(x)
        result = a[0:crossover_point] + b[crossover_point:]
        return self.from_string(result)
