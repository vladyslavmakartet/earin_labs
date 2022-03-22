from bin_vec import BinaryVector
import equation
import numpy
from RouletteWheelSelection import RouletteWheelSelection

def generate_population(_dim, _int_d, _population_size):
    population = []
    pow = 2**(_int_d)
    for i in range(_population_size):
        x = numpy.random.randint(-pow, pow, _dim)
        population.append(x)
    return numpy.asarray(population)
    
def main():
    a = BinaryVector(0)
    b = BinaryVector(-1)
    print(a)
    print(b)
    g = a.random_crossover(b)
    print(g)
    
    
    pop = generate_population(3, 3, 50)
    a = numpy.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = numpy.matrix([[1], [2], [3]])
    c = 2
    x = numpy.matrix([[1], [2], [3]])

    example_g = equation.Function_G(a, b, c)
    print("G Value:", example_g.get_value(x))
    temp = RouletteWheelSelection(pop, 50, example_g)
    print(temp)

if __name__ == "__main__":
    main()
    
    




