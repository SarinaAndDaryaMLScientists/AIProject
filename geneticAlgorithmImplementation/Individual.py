import numpy as np
import random
import copy
import main


def calCNF(genes):
    return main.howCloseWeWereToAnswer(genes)


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
