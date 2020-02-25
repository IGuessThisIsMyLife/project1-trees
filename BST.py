#Jonathan Nunes
#Project 1: Trees

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
        
def deleteRec(root, node):
    """Recursive Deletion"""
    pass

def findNextRec(root, node):
    """Recursive Find Next"""
    pass

def findPrevRec(root, node):
    """Recursive Find Prev"""
    pass

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
    while node.data < root.data:
        if root.left is None:
            root.left = node
            break
        root = root.left
    while node.data > root.data:
        if root.right is None:
            root.right = node
            break
        root = root.right
        

def deleteIter(root, node):
    """Iterative Deletion"""
    pass

def findNextIter(root, node):
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

def sort(root):
    """Sort"""
    pass

def display(root):
    """Prints All Nodes"""
    if root is None:
        return
    display(root.left)
    print(root.data)
    display(root.right)
  
def getRandomArray(n):
    """Create Randomly Filled Array"""
    temp = random.randint(0, 999)
    arr = [None]*n
    for i in range(n):
        while temp in arr:
            temp = random.randint(0, 999)
        arr[i] = temp
    return arr
  
def getSortedArray(n):
    """Created Sorted Array"""
    arr = [None]*n
    for i in range(n):
        arr[i] = n - i
    return arr

root = Node(50)
insertIter(root, Node(10))
insertIter(root, Node(75))
insertIter(root, Node(90))
insertIter(root, Node(15))
insertIter(root, Node(1))
insertIter(root, Node(60))
insertIter(root, Node(29))
display(root)
findMinRec(root)
findMaxRec(root)
#print(getRandomArray(10))
#print(getSortedArray(10))
