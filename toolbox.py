
from random import *

seed()


def gen_idx(start, stop):
    x = randrange(start, stop)
    return x


def gen_individual(target):
    new_sample = []
    for i in range(len(target)):
        new_sample.append(chr(randrange(32, 127)))

    return new_sample


def initialise_population(size, target):
    population = []
    for i in range(size):
        population.append(gen_individual(target))

    return population


def evaluate(target, subject):
    fitness = 0
    if len(target) == len(subject):
        for i in range(len(target)):
            if subject[i] == target[i]:
                fitness += 1
            else:
                pass
    else:
        print('Error, test and subject do not coincide')

    return fitness


def mutate(subject):
    if len(subject) <= 0:
        print('error, subject length not valid')
    else:
        for i in range(len(subject)):
            if randrange(0, len(subject)) == 1:
                subject[i] = chr(randrange(32, 127))
            else:
                pass

    return subject


def hill_climber(target, individual1, individual2):
    champion = []
    challenger = []
    if evaluate(target, individual1) > evaluate(target, individual2):
        champion, challenger = individual1, individual2
    else:
        champion, challenger = individual2, individual1

    return champion, challenger


def crossover(parent1, parent2):
    child = []
    if len(parent1) and len(parent2) <= 0:
        print('error, subject length not valid')
    else:
        for i in range(len(parent1)):
            if randrange(0, 2) == 0:
                child.append(parent1[i])
            else:
                child.append(parent2[i])

    # print(parent1)
    # print(parent2)
    # print(child)
    return child
