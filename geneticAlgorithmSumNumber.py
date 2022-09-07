from numpy.random import random, randint
import os
# goals : a+b+c+d+e=375
# genetics : a, b, c, d, e real num
# fitness : absolute error


def genetic(length, min_val, max_val):
    return [randint(min_val, max_val) for num in range(length)]


def fitness(genetic, desiredTarget):
    sum = 0
    for gen in genetic:
        sum += gen
    return (abs(sum - desiredTarget))


def population(numPop, length, min_val, max_val):
    return [genetic(length, min_val, max_val) for gen in range(numPop)]


def createParent(population, desiredTarget):
    # We choose 2 best genetic to be parents
    parents = [(fitness(genetic, desiredTarget), genetic) for genetic in population]
    parents.sort()
    return parents, parents[:2]


def createChildren(parents):
    fixedPoint = round(len(parents[0][1]) / 2)
    child1 = parents[0][1][:fixedPoint] + parents[1][1][fixedPoint:]
    child2 = parents[0][1][fixedPoint:] + parents[1][1][:fixedPoint]
    return [child1, child2]


def mutation(children, chanceToMutate = 0.6):
    for i in range(len(children)):
        for j in range(len(children[i])):
            if chanceToMutate > random(size = 1):
                if min(children[i]) != max(children[i]):
                    children[i][j] = randint(min(children[i]), max(children[i]))
                elif min(children[i]) == max(children[i]):
                    children[i][j] = randint(min(children[i]), max(children[i]) + 1)
    return children


def regeneration(population, children, desiredTarget):
    sortedChildren = [(fitness(child, desiredTarget), child) for child in children]
    sortedChildren.sort()
    newPop = []
    for index in range(len(children)):
        population[-(index+1)] = sortedChildren[index]
    for gen in population:
        newPop.append(gen[1])
    return newPop


def main():
    clear = lambda: os.system("cls")
    desiredTarget = 375
    numPop = 5
    length = 5
    min_val = 5
    max_val = 100
    pop = population(numPop, length, min_val, max_val)
    isLoop = True
    iteration = 0

    while isLoop:
        newPop, parents = createParent(pop, desiredTarget)
        children = createChildren(parents)
        mut = mutation(children)
        pop = regeneration(newPop, mut, desiredTarget)
        clear()
        print("<===========================>")
        print(f"Iterasi ke-{iteration+1}")
        print("Desired Target:", desiredTarget)
        print("Fitness:", newPop[0][0])
        print("Gen:", newPop[0][1])
        print("<===========================>")
        if newPop[0][0] == 0:
            isLoop = False
        iteration += 1


if __name__ == "__main__":
    main()