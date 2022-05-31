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
