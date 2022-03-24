

from random import randint, random
from typing import Tuple
from numpy import binary_repr


class BinaryVectorOverflow(Exception):
    pass

class BadProbabilityValue(Exception):
    pass

class BinaryVector:

    def __init__(self, value: int, width_limit: int) -> None:
        max_bit_value = value.bit_length()
        if value >= 0:
            max_bit_value += 1
        if max_bit_value > width_limit:
            raise BinaryVectorOverflow("Representation of a number requires too many bits")
        self.value = value
        self.width_limit = width_limit

    def __str__(self) -> str:
        return binary_repr(self.value, self.width_limit)

    def from_string(self, x: str) -> "BinaryVector":
        value = int(x, base=2)
        if value >= 2 ** (self.width_limit - 1): # it will be 1... so it will be ngative in U2
            value -= 2 ** self.width_limit # making it negative
        return BinaryVector(value, width_limit=self.width_limit)

    def crossover(self, x: "BinaryVector", crossover_point: int) -> Tuple["BinaryVector", "BinaryVector"]:
        a = str(self)
        b = str(x)
        result = a[0:crossover_point] + b[crossover_point:]
        result2 = b[0:crossover_point] + a[crossover_point:]
        print("R1", result)
        print("R2", result2)
        print("Cross", crossover_point)
        print("len", len(a))
        if crossover_point == 0:
            result = b
            result2 = a
        return self.from_string(result), self.from_string(result2)

    def random_crossover(self, x: "BinaryVector") -> Tuple["BinaryVector", "BinaryVector"]:
        rand_result = randint(0, self.width_limit)
        return self.crossover(x, rand_result)

    def mutate(self, probability: float) -> None:
        if probability < 0 or probability > 1:
            raise BadProbabilityValue("Given probability is out of 0 to 1 range")
        value = self.value
        for i in range(self.width_limit):
            if probability > random():
                value ^= 1 << i
        self.value = value
