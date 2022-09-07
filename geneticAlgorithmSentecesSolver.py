import numpy as np
from numpy.random import randint
import os
import random
import string
# goals : generate sentences as given sentences (ex. "rian hendy")
# genetics : string
# fitness : (sum(np.all(givenSentence, gen)) / len(givenSentences))*100.0
# Note : Generate genetik pada program ini dibatasi hanya pada sebarang ascii_letters
# + digits + whitespace karena keterbatasan kekuatan laptop:)


def genetic(desiredSentence):
    # Create random string with length same as givenSentences length
    length = len(desiredSentence)
    # char = string.digits
    char = string.ascii_letters+string.digits+string.whitespace
    gen = [*"".join(random.choice(char) for i in range(length))]
    return gen



def fitness(gen, desiredSentences):
    sum = 0
    for i in range(len(desiredSentences)):
        if gen[i] == desiredSentences[i]:
            sum += 1
    return ((sum / len(desiredSentences))*100.0)


def population(numPop, desiredSentence):
    return [*[genetic(desiredSentence) for x in range(numPop)]]


def createParent(population, desiredSentence):
    # We choose 2 best genetic to be parents
    parents = [(fitness(gen, desiredSentence), [*gen]) for gen in population]
    parents.sort(reverse = True)
    return parents, parents[:2]


def createChildren(parents):
    fixedPoint = round(len(parents[0][1]) / 2)
    child1 = parents[0][1][:fixedPoint] + parents[1][1][fixedPoint:]
    child2 = parents[0][1][fixedPoint:] + parents[1][1][:fixedPoint]
    return [child1, child2]


def mutation(children, chanceToMutate = 0.2):
    for i in range(len(children)):
        for j in range(len(children[i])):
            if chanceToMutate > random.random():
                # char = string.digits
                char = string.ascii_letters+string.whitespace
                children[i][j] = random.choice(char)
    return children


def regeneration(population, children, desiredSentence):
    sortedChildren = [(fitness(child, desiredSentence), child) for child in children]
    sortedChildren.sort(reverse = True)
    newPop = []
    for index in range(len(children)):
        population[-(index+1)] = sortedChildren[index]
    for gen in population:
        newPop.append(gen[1])
    return newPop


def main():
    clear = lambda: os.system("cls")
    desiredSentence = "Rian Hendy"
    numPop = 5
    pop = population(numPop, desiredSentence)
    iteration = 0
    isLoop = True

    while isLoop:
        newPop, parents = createParent(pop, desiredSentence)
        children = createChildren(parents)
        mut = mutation(children)
        pop = regeneration(newPop, mut, desiredSentence)
        clear()
        print("<================================>")
        print(f"Iterasi ke-{iteration+1}")
        print(f"Desired sentence: {desiredSentence}")
        print(f"Fitness: {newPop[0][0]}")
        print("Gen:", "".join(newPop[0][1]))
        print("<================================>")
        if newPop[0][0] == 100.0:
            isLoop = False
        iteration += 1


if __name__ == "__main__":
    main()