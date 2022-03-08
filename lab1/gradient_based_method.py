import numpy
import time
import equation

def gradient_based_method(function: equation.Function_G, current_sol, choice) -> numpy.array:
    if choice == '2':
        current_sol = numpy.random.uniform(int(current_sol[0]), int(current_sol[1]), function.get_b.size)
    
    rate = 0.01             # Learning rate
    precision = 0.000001    # This tells us when to stop the algorithm
    max_iteration = 10000   # Maximum number of iterations
    iteration = 0           # Iteration counter
    max_exe_time = 10       # Maximum computation time in seconds.
    exe_time = 0
    step_size = 1

    start_time = time.time()
    while step_size > precision and iteration < max_iteration and exe_time < max_exe_time:
        prev_x = current_sol
        current_sol = current_sol - function.get_gradient_value(prev_x) * rate
        step_size = abs(function.get_value(current_sol) - function.get_value(prev_x))
        iteration = iteration + 1
        exe_time = time.time() - start_time
    return current_sol