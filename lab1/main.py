import numpy
import equation
from methods import NewtonMethod, GradientDescent, BREAK_ITERATIONS

def main() -> None:
    example_function = equation.Function_F(0.25, 2, 3, 1)
    print("F Type:", example_function.get_x_type())
    print("F Value for 2:", example_function.get_value(2))
    print("F Derivative for 2:", example_function.get_gradient_value(2))
    a = numpy.matrix([[1, 2, 3], [1, 5, 3], [1, 2, 3]])
    b = numpy.matrix([[1], [2], [3]])
    c = 1
    x = numpy.matrix([[1], [2], [3]])
    example_g = equation.Function_G(a, b, c)
    print("G Type:", example_g.get_x_type())
    print("G Value:", example_g.get_value(x))
    print("G Derivative:", example_g.get_gradient_value(x))
    
    print('============================================================')
    print(GradientDescent.calculate_minimum(example_function, 1, BREAK_ITERATIONS, 200))
    print(NewtonMethod.calculate_minimum(example_function, 1, BREAK_ITERATIONS, 200))
    print('============================================================')
if __name__ == "__main__":
    main()