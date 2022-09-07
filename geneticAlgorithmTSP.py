from unicodedata import numeric
import numpy as np
from random import random, randint
from time import time
import matplotlib.pyplot as plt
from pandas import DataFrame
from IPython.display import display
import os


def randomCityLocation(numCity):
    x = []
    y = []
    for i in range(numCity):
        x.append(randint(0, 100))
        y.append(randint(0, 50))
    return x, y


def plotResult(x, y):
    plt.scatter(x, y)
    plt.show()


def createGenetic(numCity):
    return np.random.permutation(numCity).tolist()


def createPopulation(numPop, numCity):
    population = []
    for i in range(numPop):
        population.append(createGenetic(numCity))
    return population


def createDistanceMatrix(x, y):
    distMatrix = []
    for i in range(len(x)):
        row = []
        for j in range(len(y)):
            row.append(round(np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)))
        distMatrix.append(row)
    return distMatrix


def calculateFitness(genetic, distMatrix):
    fitness = 0
    for i in range(len(genetic) - 1):
        fitness += distMatrix[genetic[i]][genetic[i+1]]
    fitness += distMatrix[genetic[-1]][genetic[0]]
    return fitness


def selection(population, distMatrix):
    newPop = [(calculateFitness(gen, distMatrix), gen) for gen in population]
    parents = newPop.copy()
    parents.sort()
    return parents, parents[:2]

# x, y = randomCityLocation(5)
# d = createDistanceMatrix(x, y)
# p = createPopulation(5, 5)
# p1, p2 = selection(p, d)
# print("P", p)


def crossover(parents):
    randPoint = randint(0, len(parents[0][1]) - 2)
    child1 = parents[0][1].copy()
    child2 = parents[1][1].copy()
    crossover1 = parents[0][1][:randPoint]
    crossover2 = parents[1][1][randPoint:]
    # First Child
    for city in crossover1:
        child2.remove(city)
    crossover1 = np.random.permutation(crossover1).tolist()
    child2 = child2 + crossover1
    # Second Child
    for city2 in crossover2:
        child1.remove(city2)
    crossover2 = np.random.permutation(crossover2).tolist()
    child1 = child1 + crossover2
    return [child1, child2]


def mutation(children):
    for child in children:
        randInt1 = randint(0, len(child) - 2)
        randInt2 = randint(0, len(child) - 2)
        child[randInt1], child[randInt2] = child[randInt2], child[randInt1]
    return children


def regeneration(population, children, distMatrix):
    n = 0
    sortedChildren = [(calculateFitness(gen, distMatrix), gen) for gen in children]
    sortedChildren.sort()
    newSort = []
    newPop = []
    for item in sortedChildren:
        newSort.append(item[1])
    for i in range(len(population) - len(children)):
        newPop.append(population[i])
    for sort in newSort:
        newPop.append(sort)
    # newPop = population[:(len(population) - len(children))] + newSort
    witFit = [(calculateFitness(gen, distMatrix), gen) for gen in newPop]
    return newPop, witFit


def main():
    clear = lambda: os.system("cls")
    numCity = 5
    numPop = 7
    x, y = randomCityLocation(numCity)
    d = createDistanceMatrix(x, y)
    initPop = createPopulation(numPop, numCity)
    print("InitPop:\n", initPop)

    for i in range(100):
        print("\nIterasi ke-", i+1)
        selection1, parents = selection(initPop, d)
        print("initPopWFitness:\n", selection1)
        print("Parents:\n", parents)
        child = crossover(parents)
        print("Anak dihasilkan:\n", child)
        mutateChild = mutation(child)
        print("Mutasi Anak:\n", mutateChild)
        initPop, wit = regeneration(initPop, mutateChild, d)
        print("Regenerasi:\n", initPop)
        print("With:\n", wit)

    print("D:\n", d)




if __name__ == "__main__":
    main()