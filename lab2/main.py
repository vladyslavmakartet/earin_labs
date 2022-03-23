from bin_vec import BinaryVector
import equation
import numpy
from RouletteWheelSelection import roulette_wheel_selection, match_parents, generate_population

def main():
    a = BinaryVector(0)
    b = BinaryVector(-1)
    print("a", a)
    a.mutate(0.3)
    print("Mutated", a)
    print("b", b)
    g, g2 = a.random_crossover(b)
    print("G", g, g2)
    
    pop = generate_population(3, 3, 50)
    #print("pop", pop)
    #print("pop len", len(pop))
    a = numpy.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = numpy.matrix([[1], [2], [3]])
    c = 2
    x = numpy.matrix([[1], [2], [3]])

    example_g = equation.Function_G(a, b, c)
    temp = roulette_wheel_selection(pop, 50, example_g)
    new_childs = match_parents(pop, temp, 6, 0.1, 0.1)
    print("Childs", new_childs)

if __name__ == "__main__":
    main()
