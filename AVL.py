# Jonathan Nunes
# Project 1 (Part 2): AVL Tree

import random

class Node:
    def __init__(self, n):
        """Node Constructor"""
        self.left = None
        self.right = None
        self.data = n


def insertRec(root, node):
    """Recursive Insertion"""
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insertRec(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertRec(root.left, node)


def deleteRec(root, n):
    """Recursive Deletion"""
    


def findNextRec(root, n):
    """Recursive Find Next"""
    if root.data < n:
        print("Recursively Found Next: %i" % root.data)
        return
    if root.left is not None:
        findNextRec(root.left, n)
    if root.right is not None:
        findNextRec(root.right, n)


def findPrevRec(root, n):
    """Recursive Find Prev"""
    if root.data > n:
        print("Recursively Found Prev: %i" % root.data)
        return
    if root.left is not None:
        findPrevRec(root.left, n)
    if root.right is not None:
        findPrevRec(root.right, n)


def findMinRec(root):
    """Recursive Find Min"""
    if root.left is None:
        print("Recursively Found Min: %i" % root.data)
        return
    else:
        findMinRec(root.left)


def findMaxRec(root):
    """Recursive Find Max"""
    if root.right is None:
        print("Recursively Found Max: %i" % root.data)
        return
    else:
        findMaxRec(root.right)


def insertIter(root, node):
    """Iterative Insertion"""
    while True:
        if root.data < node.data:
            if root.right is None:
                root.right = node
                return
            else:
                root = root.right
        else:
            if root.left is None:
                root.left = node
                return
            else:
                root = root.left


def deleteIter(root, node):
    """Iterative Deletion"""
    pass


def findNextIter(root, n):
    """Iterative Find Next"""
    pass


def findPrevIter(root, node):
    """Iterative Find Prev"""
    pass


def findMinIter(root):
    """Iterative Find Min"""
    while root.left is not None:
        root = root.left
    print("Iteratively Found Min: %i" % root.data)


def findMaxIter(root):
    """Iterative Find Max"""
    while root.right is not None:
        root = root.right
    print("Iteratively Found Max: %i" % root.data)


def sort(arr):
    """Sorting Function"""
    tree = Node(arr[0])
    for item in arr:
        if item == tree.data:
            continue
        insertRec(tree, Node(item))
    ret = []
    return treeSort(tree, ret)


def treeSort(root, ret):
    """Helper Function Building Sorted Array Recursively"""
    if root is None:
        return
    treeSort(root.left, ret)
    ret.append(root.data)
    treeSort(root.right, ret)
    return ret


def display(root):
    """For My Testing Purposes: Prints All Nodes"""
    if root is None:
        return
    display(root.left)
    print(root.data)
    display(root.right)


def getRandomArray(n):
    """Create Randomly Filled Array"""
    temp = random.randint(0, 999)
    arr = [None] * n
    for i in range(n):
        while temp in arr:
            temp = random.randint(0, 999)
        arr[i] = temp
    return arr


def getSortedArray(n):
    """Created Sorted Array"""
    arr = [None] * n
    for i in range(n):
        arr[i] = n - i
    return arr

print("Test Recursive Functions")
rootRec = Node(50)
insertRec(rootRec, Node(10))
insertRec(rootRec, Node(75))
insertRec(rootRec, Node(90))
insertRec(rootRec, Node(15))
insertRec(rootRec, Node(30))
insertRec(rootRec, Node(66))
insertRec(rootRec, Node(17))
insertRec(rootRec, Node(400))
insertRec(rootRec, Node(1))
insertRec(rootRec, Node(60))
insertRec(rootRec, Node(29))
display(rootRec)
findMinRec(rootRec)
findMaxRec(rootRec)
findNextRec(rootRec, 17)
findPrevRec(rootRec, 75)
deleteRec(rootRec, 400)
deleteRec(rootRec, 60)
deleteRec(rootRec, 50)
display(rootRec)

print("\nTest Iterative Functions")
rootIter = Node(50)
insertIter(rootIter, Node(10))
insertIter(rootIter, Node(75))
insertIter(rootIter, Node(90))
insertIter(rootIter, Node(15))
insertIter(rootIter, Node(30))
insertIter(rootIter, Node(66))
insertIter(rootIter, Node(17))
insertIter(rootIter, Node(400))
insertIter(rootIter, Node(1))
insertIter(rootIter, Node(60))
insertIter(rootIter, Node(29))
display(rootIter)
findMinIter(rootIter)
findMaxIter(rootIter)
findNextIter(rootIter, 17)
findPrevIter(rootIter, 75)
deleteIter(rootIter, 400)
deleteIter(rootIter, 60)
deleteIter(rootIter, 50)
display(rootIter)

#Test Question 2 & 3
randomArr = getRandomArray(10)
print(randomArr)
sortedArr = sort(randomArr)
print(sortedArr)

print(getSortedArray(10))
