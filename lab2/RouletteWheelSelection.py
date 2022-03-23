from typing import List
import equation
import numpy as np

def RouletteWheelSelection(pop: List[np.matrix], pop_size: int, equation: equation.Function_G):
    fit = []
    for chromosome in pop:
        fit.append(equation.get_value(chromosome))

    max_fit = max(fit)
    min_fit = min(fit)
    parents = []

    # Rescale to [0, 1]
    fit_rescale = []
    sum = 0
    for f in range(len(fit)):
        if max_fit == min_fit:
            res_val = 1
        else:
            res_val = (fit[f] - min_fit) / (max_fit - min_fit)
        sum += res_val
        fit_rescale.append((res_val, pop[f]))
        
    wheel = []
    prev = 0
    if sum != 0:
        for fit_res in fit_rescale:
            curr = prev + (fit_res[0] / sum)
            wheel.append(curr)
            prev = curr

    # Selecting parents based on roulette wheel
    for _ in range(pop_size):
        spin = np.random.uniform(0, 1)
        i = 0
        while i in range(len(wheel)) and wheel[i] < spin:
            i = i + 1

        parent = fit_rescale[i][1]
        parents.append(parent)

    return parents