import numpy as np
import random
import copy
#Hello, sorry for not testing it, i actually can't undrestand the problem in my code.
lines = np.loadtxt("database.cnf", dtype=int, delimiter="  ", unpack=False)
temp = ""

# to access each variable use this line :
cnf = []
cnfI = []
mxNum = -1
for i in np.nditer(lines):
    if i == 0:
        cnf.append(cnfI)
        cnfI = []
    else:
        cnfI.append(int(i))

gene_len = 101
iterations = 100000
pop_len = 20


def generate_random_population(pl, gl):
    ls = []
    for x in range(pl):
        ls.append(np.random.randint(0, 2, gl).tolist())
    return ls


def satisfyCon(b, gene):
    if b > 0 and gene[b] == 1:
        return True
    if b < 0 and gene[b] == 0:
        return True
    return False


def get_fitness(gene):
    score = 0
    for a, b, c in cnf:
        if satisfyCon(a, gene) and satisfyCon(b, gene) and satisfyCon(c, gene):
            score = score + 1
    return score


def calculate_fitness_score(pop):
    score = 0
    for j in range(len(pop)):
        score += get_fitness(pop[j])
    return score


def selection(population1):
    maximum = -1
    secondMax = -1
    maximumIndex = -1
    secondMaxIndex = -1
    index = 0
    for gen in population1:
        if get_fitness(gen) > maximum:
            secondMax = maximum
            secondMaxIndex = maximumIndex
            maximum = get_fitness(gen)
            maximumIndex = index
        index = index + 1
    return population1[maximumIndex], population1[secondMaxIndex]


# calculate_fitness_score(population)
def crossover(p1, p2):
    firstHalf = p1[:len(p1) // 2]
    secondHalf = p2[len(p2) // 2]
    return [firstHalf, secondHalf]


population = generate_random_population(pop_len, gene_len)
crossoverRate = 0.05
mutationRate = 0.01


def mutate(selectedPopulation1):
    rand = random.randint(0, len(selectedPopulation1))
    if selectedPopulation1[rand] == 1:
        selectedPopulation1[rand] = 0
    else:
        selectedPopulation1[rand] = 1


for n in range(iterations):
    x = np.random.random()
    selectedPopulation = selection(population)
    for c in crossover(selectedPopulation):
        if x < mutationRate:
            mutate(selectedPopulation)
