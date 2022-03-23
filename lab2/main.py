from bin_vec import BinaryVector
import equation
import numpy
from RouletteWheelSelection import RouletteWheelSelection, match_parents

def generate_population(_dim, _int_d, _population_size):
    population = []
    pow = 2**(_int_d)
    for _ in range(_population_size):
        x = numpy.random.randint(-pow, pow, _dim)
        x = numpy.asmatrix(x)
        population.append(x.transpose())
    return population

def main():
    a = BinaryVector(0)
    b = BinaryVector(-1)
    print("a", a)
    a.mutate(0.3)
    print("Mutated", a)
    print("b", b)
    g = a.random_crossover(b)
    print(g)
    
    
    pop = generate_population(3, 3, 50)
    print("pop", pop)
    print("pop len", len(pop))
    a = numpy.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = numpy.matrix([[1], [2], [3]])
    c = 2
    x = numpy.matrix([[1], [2], [3]])

    example_g = equation.Function_G(a, b, c)
    temp = RouletteWheelSelection(pop, 50, example_g)
    new_childs = match_parents(temp, 2, 0.1)
    print("Childs", new_childs)

if __name__ == "__main__":
    main()
