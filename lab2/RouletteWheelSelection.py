from random import randint
from typing import List
import equation
import numpy as np

from bin_vec import BinaryVector

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

def match_parents(parents: List[np.matrix], count: int, mutation_probability: float) -> List[np.matrix]:
    even = count % 2

    iterations = count // 2 + even # each iteration produces 2 childs from 2 parents
    childs = []
    for _ in range(iterations):
        parent1 = parents[randint(0, len(parents) - 1)]
        parent2 = parents[randint(0, len(parents) - 1)]
        new_matrix1 = []
        new_matrix2 = []
        for row1, row2 in zip(parent1, parent2):
            value1 = np.asscalar(row1)
            value2 = np.asscalar(row2)
            value1 = BinaryVector(value1)
            value2 = BinaryVector(value2)
            value1, value2 = value1.random_crossover(value2)
            value1.mutate(mutation_probability)
            value2.mutate(mutation_probability)
            new_matrix1.append(value1.value)
            new_matrix2.append(value2.value)
        new_matrix1 = np.asmatrix(new_matrix1)
        new_matrix2 = np.asmatrix(new_matrix2)
        childs.append(new_matrix1.transpose())
        childs.append(new_matrix2.transpose())
    if even == 1:
        childs.pop() # if not even then we have one childs too much
    return childs
