from random import randint, random
from typing import List
import equation
import numpy as np

from bin_vec import BinaryVector
from equation import Function_G

def generate_population(dim, d, population_size):
    population = []
    print("d", d)
    power = pow(2, d-1)
    print("power", power)
    for _ in range(population_size):
        x = np.random.randint(-power, power-1, dim)
        x = np.asmatrix(x)
        population.append(x.transpose())
    return population

def roulette_wheel_selection(pop: List[np.matrix], pop_size: int, equation: equation.Function_G):
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

def match_parents(current_population: List[np.matrix], parents: List[np.matrix], count: int, mutation_probability: float, crossover_probability: float, d: int) -> List[np.matrix]:
    iterations = count // 2 # each iteration produces 2 childs from 2 parents
    childs = []
    for _ in range(iterations):
        crossover = random() < crossover_probability
        parent1 = parents[randint(0, len(parents) - 1)]
        parent2 = parents[randint(0, len(parents) - 1)]
        new_matrix1 = []
        new_matrix2 = []
        if not crossover:
            continue
        for row1, row2 in zip(parent1, parent2):
            value1 = np.asscalar(row1)
            value2 = np.asscalar(row2)
            value1 = BinaryVector(value1, d)
            value2 = BinaryVector(value2, d)
            value1, value2 = value1.random_crossover(value2)
            value1.mutate(mutation_probability)
            value2.mutate(mutation_probability)
            new_matrix1.append(value1.value)
            new_matrix2.append(value2.value)
        new_matrix1 = np.asmatrix(new_matrix1)
        new_matrix2 = np.asmatrix(new_matrix2)
        childs.append(new_matrix1.transpose())
        childs.append(new_matrix2.transpose())
    for parent in current_population:
        new_matrix = []
        for row in parent:
            value = np.asscalar(row)
            value = BinaryVector(value, d)
            value.mutate(mutation_probability)
            new_matrix.append(value.value)
        new_matrix = np.asmatrix(new_matrix)
        parent = new_matrix.transpose()
    new_population = [*childs, *current_population] # parents at the end and we drop end, so FIFO
    new_population = new_population[0:count] # we drop the oldest parents
    return new_population

def run_algorithm(
        dimension: int,
        population_size: int,
        d: int,
        mutation_probability: float,
        crossover_probability: float,
        iterations: int,
        function_g: Function_G):
    population = generate_population(dimension, d, population_size)
    for _ in range(iterations):
        roulette_result = roulette_wheel_selection(population, population_size, function_g)
        population = match_parents(population, roulette_result, population_size, mutation_probability, crossover_probability, d)
    return population