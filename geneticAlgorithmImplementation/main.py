import numpy as np
import random
import copy
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
        if abs(int(i)) > mxNum:
            mxNum = abs(int(i))
        cnfI.append(int(i))
# print(cnf)
# print(mxNum) #first optimization failed. the number 100 is used in these numbers, so instead we will look for actual optimization
arr = np.zeros(101)


def satifyCondition(a, x):
    if x != 0:
        if a > 0:
            return True
        else:
            return False
    else:
        if a > 0:
            return False
        else:
            return True


def satisfiesAllCnf(arr1, cnf1):
    for a, b, c in cnf1:
        res = satifyCondition(a, arr1[abs(a)]) or satifyCondition(b, arr1[abs(b)]) or satifyCondition(c, arr1[abs(c)])
        if not res:
            return False
    return True


# print(satisfiesAllCnf(arr, cnf))
# boolExpressionValues = [0, 1]

def howCloseWeWereToAnswer(arr1):
    score = 0
    for a, b, c in cnf:
        res = satifyCondition(a, arr1[abs(a)]) or satifyCondition(b, arr1[abs(b)]) or satifyCondition(c, arr1[abs(c)])
        if res:
            score = score + 1
    return score


def printPopulationAndFitnessScore(genCnt, population):
    print("current generation is the {} generation with the {} population".format(genCnt, population.fitnessScore))


def copyArray(bestGene):
    arr1 = []
    for item in bestGene:
        arr1.append(item)
    return arr1


def evaluate(population):
    bestGene = population.getBestIndividual().copy()
    u = copyArray(bestGene)
    for k in range(101):
        u = copyArray(bestGene)
        if bestGene[k] == 1:
            u[k] = 0
        else:
            u[k] = 1
        if howCloseWeWereToAnswer(u) > howCloseWeWereToAnswer(bestGene):
            bestGene[k] = u[k]
    return bestGene


def geneticAlgorithm(arr1):
    genCnt = 0
    population = Population.Population()
    printPopulationAndFitnessScore(genCnt, population)
    while True:
        if population.fitnessScore == 101:
            print("successfully generated the population!")
            break;
        else:
            print("starting selection")
            population.selectBestAndSecondBestAndThirdBest()
            print("starting crossover")
            population.doCrossOverBetweenGen1And2Gene2And3AndGene1And3()
            print("checking if evaluation condition is met")
            rand = random.random()
            if rand > 0.7:
                print("evaluation started")
                evaluate(population)
                print("evaluation completed")





def calCNF(genes):
    return howCloseWeWereToAnswer(genes)


class Individual:
    def __init__(self):
        self.geneLen = 101
        self.fitness = 0
        self.genes = np.zeros(101)
        for i in range(0, self.geneLen):
            rand = random.random()
            if rand < 0.5:
                self.genes[i] = 0
            else:
                self.genes[i] = 1

    def calculateFitness(self):
        self.fitness = calCNF(self.genes)
        return self.fitness

    def copy(self):
        return copy.deepcopy(self)
class Population():
    def __init__(self):
        self.popSize = 0
        self.individuals = []  # array of individuals in a gene.
        self.geneLen = 101
        self.fitnessScore = 0

    def getFitnessScore(self):
        score = 0
        for i in range(len(self.individuals)):
            score = score + self.individuals[i].calculateFitness()

    def getBestGene(self):
        maxFitnessIndex = self.calMaxFitness()
        return self.individuals[maxFitnessIndex]

    def calMaxFitness(self):
        mx, mxIndex = -1, -1
        for x in range(len(self.individuals)):
            if self.individuals[x].fitness > mx:
                mx = self.individuals[x].fitness
                mxIndex = x
        return mxIndex
