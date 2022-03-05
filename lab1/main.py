import numpy
import equation

def main() -> None:
    example_function = equation.Function_F(1, 2, 3, 4)
    print("F Type:", example_function.get_x_type())
    print("F Value for 2:", example_function.get_value(2))
    a = numpy.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = numpy.matrix([[1], [2], [3]])
    c = 2
    x = numpy.matrix([[1], [2], [3]])
    example_g = equation.Function_G(a, b, c)
    print("G Type:", example_g.get_x_type())
    print("G Value:", example_g.get_value(x))

if __name__ == "__main__":
    main()