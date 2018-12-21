import numpy as np
import time
from toolbox import *

target = 'methinks it is like a weasel'
list_target = list(target)
pop_size = 500
fitness_array = []
count = 10000
epoch = 0
if __name__ == "__main__":

    # initial = gen_individual(target)

    population = initialise_population(pop_size, list_target)
    for i in range(pop_size):
        fitness_array.append(evaluate(list_target, population[i]))

    max_fitness = np.argmax(fitness_array)

    while max_fitness is not len(list_target):
        # choose 2 random individuals and compare fitness
        parent1, loser1 = hill_climber(list_target,
                                       population[gen_idx(0, pop_size)],
                                       population[gen_idx(0, pop_size)])

        parent2, loser2 = hill_climber(list_target,
                                       population[gen_idx(0, pop_size)],
                                       population[gen_idx(0, pop_size)])

        child = crossover(parent1, parent2)
        child = mutate(child)
        # mutate to create a child and assess fitness

        child_fitness = evaluate(list_target, child)
        if max_fitness < child_fitness:
            max_fitness = child_fitness
            print(child)
            print('new max fitness = ', max_fitness)

        else:
            pass

        count += 1
        if count >= 10000:
            epoch += 1
            count = 0
            print(epoch, 'fit=', max_fitness)
            if epoch % 100 == 0:
                print(population)
            else:
                pass
        else:
            pass

        # replace a less fit individual
        subject1, subject2 = randrange(0, pop_size - 1), randrange(0, pop_size - 1)
        if evaluate(list_target, population[subject1]) >= evaluate(list_target, population[subject2]):
            population[subject2] = child
        else:
            population[subject1] = child















