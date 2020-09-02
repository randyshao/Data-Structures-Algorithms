# Name: Randy Shao
# Student Number: 20100992

import assn3
import random

def exp1():
    set = [250, 500, 1000, 2000, 4000, 8000, 16000]

    for n in set:
        avgDepthList = []
        maxDepthList = []
        # Initializes a permutation of length n
        for i in range(1, 500):
            permList = [0] * n
            permTree = []
            # Fills the list with values
            for i in range(n):
                permList[i] = i + 1
            # Rearranges permutation
            while len(permList):
                size = len(permList)
                index = random.randint(0, size - 1)
                permList[index], permList[size - 1] = permList[size - 1], permList[index]
                num = permList.pop()
                permTree.append(num)
            bst = assn3.Tree()
            for node in permTree:
                bst.insert(node)
            avgDepthList.append(bst.averageDepth())
            maxDepthList.append(bst.maxDepth(bst.root))

        # Calculates average of average/max of n
        totalAvg = 0
        totalMax = 0
        for i in avgDepthList:
            totalAvg += i
        avgAvgDepth = totalAvg / len(avgDepthList)
        for i in maxDepthList:
            totalMax += i
        avgMaxDepth = totalMax / len(maxDepthList)

        print("Average of average depths of n: ", avgAvgDepth)
        print("Average of max depths of n: ", avgMaxDepth)

        # Calculates max of average/max of n
        maxAvg = 0
        maxMax = 0
        for i in avgDepthList:
            if i > maxAvg:
                maxAvg = i
        for i in maxDepthList:
            if i > maxMax:
                maxMax = i
        print("Max of average depths of n: ", maxAvg)
        print("Max of max depths of n: ", maxMax)

def exp2():
    set = [250, 500, 1000, 2000, 4000, 8000, 16000]

    for n in set:
        avgDepthList = []
        maxDepthList = []
        # Initializes a permutation of length x
        for i in range(1, 500):
            x = (11 * n) // 10
            permList = [0] * x
            permTree = []

            # Fills the list with values
            for i in range(x):
                permList[i] = i + 1

            # Rearranges permutation
            while (len(permList)):
                size = len(permList)
                index = random.randint(0, size - 1)
                permList[index], permList[size - 1] = permList[size - 1], permList[index]
                num = permList.pop()
                permTree.append(num)
            bst = assn3.Tree()
            for node in permTree:
                bst.insert(node)
            deleteList = []
            for i in range(1, (n // 10) + 1):
                val = random.randint(1, x)
                deleteList.append(val)
            for i in deleteList:
                bst.delete(i)
            avgDepthList.append(bst.averageDepth())
            maxDepthList.append(bst.maxDepth(bst.root))

        # Calculates average of average/max of n
        totalAvg = 0
        totalMax = 0
        for i in avgDepthList:
            totalAvg += i
        avgAvgDepth = totalAvg / len(avgDepthList)
        for i in maxDepthList:
            totalMax += i
        avgMaxDepth = totalMax / len(maxDepthList)
        print("Average of average depths of n: ", avgAvgDepth)
        print("Average of max depths of n: ", avgMaxDepth)

        # Calculates max of average/max of n
        maxAvg = 0
        maxMax = 0
        for i in avgDepthList:
            if i > maxAvg:
                maxAvg = i
        for i in maxDepthList:
            if i > maxMax:
                maxMax = i
        print("Max of average depths of n: ", maxAvg)
        print("Max of max depths of n: ", maxMax)

def main():
    exp1()
    exp2()

main()

