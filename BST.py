# Jonathan Nunes
# Project 1: Trees

import random

class Node:
    def __init__(self, n):
        """Node Constructor"""
        self.left = None
        self.right = None
        self.data = n
        self.parent = None


class BST:
    def __init__(self):
        """Binary Search Tree Constructor"""
        self.root = None


    def insertRec(self, curr, node):
        """Recursive Insertion"""
        if self.root is None:
            self.root = node
        else:
            if curr.data < node.data:
                if curr.right is None:
                    curr.right = node
                    curr.right.parent = curr
                else:
                    self.insertRec(curr.right, node)
            else:
                if curr.left is None:
                    curr.left = node
                    curr.left.parent = curr
                else:
                    self.insertRec(curr.left, node)


    def deleteRec(self, curr, node):
        """Recursive Deletion"""
        if curr is None:
            return curr
        if curr.data > node.data:
            curr.left = self.deleteRec(curr.left, node)
        elif curr.data < node.data:
            curr.right = self.deleteRec(curr.right, node)
        else:
            if curr.right is None:
                temp = curr.left
                curr = None
                return temp
            elif curr.left is None:
                temp = curr.right
                curr = None
                return temp
            temp = self.findMinRec(curr.right)
            curr.data = temp.data
            curr.right = self.deleteRec(curr.right, temp)
        return curr


    def findNextRec(self, curr, node):
        """Recursive Find Next"""
        curr = self.search(self.root, node)
        if curr is None:
            return curr
        if curr.right is not None:
            return self.findMinRec(curr.right)
        if curr.parent.left.data == curr.data:
            return curr.parent
        else:
            
        

    def findPrevRec(self, curr, node):
        """Recursive Find Prev"""
        if curr.data == node.data:
            if curr.left is not None:
                return self.findMaxRec(curr.left)
        elif curr.data > node.data:
            if curr.left is not None:
                print(curr.data)
                return self.findPrevRec(curr.left, node)
        else:
            if curr.right is not None:
                print(curr.data)
                return self.findPrevRec(curr.right, node)


    def findMinRec(self, curr):
        """Recursive Find Min"""
        if curr.left is not None:
            return self.findMinRec(curr.left)
        else:
            return curr
            

    def findMaxRec(self, curr):
        """Recursive Find Max"""
        if curr.right is not None:
            return self.findMaxRec(curr.right)
        else:        
            return curr    


    def insertIter(self, curr, node):
        """Iterative Insertion"""
        if self.root is None:
            self.root = node
            return
        while True:
            if curr.data < node.data:
                if curr.right is None:
                    curr.right = node
                    curr.right.parent = curr
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                    curr.left.parent = curr
                    break
                else:
                    curr = curr.left


    def deleteIter(self, curr, node):
        """Iterative Deletion"""
        if curr is None:
            return curr
        if curr.left is None and curr.right is None:
            if curr.data == node.data:
                return None
            else:
                return curr
        


    def findNextIter(self, curr, node):
        """Iterative Find Next"""
        curr = self.search(self.root, node)
        if curr.right is not None:
            return self.findMinIter(curr.right)
        
        parent = curr.parent
        while parent is not None:
            if curr != parent.right:
                break
            curr = parent
            parent = parent.parent
        return parent


    def findPrevIter(self, curr, node):
        """Iterative Find Prev"""
        curr = self.search(self.root, node)
        if curr.left is not None:
            return self.findMaxIter(curr.left)
        
        parent = curr.parent
        while parent is not None:
            if curr != parent.left:
                break
            curr = parent
            parent = parent.parent
        return parent


    def findMinIter(self, curr):
        """Iterative Find Min"""
        while curr.left is not None:
            curr = curr.left
        return curr


    def findMaxIter(self, curr):
        """Iterative Find Max"""
        while curr.right is not None:
            curr = curr.right
        return curr


    def display(self, curr):
        """For My Testing Purposes: Prints All Nodes In Order"""
        if curr is None:
            return
        self.display(curr.left)
        print(curr.data)
        self.display(curr.right)


    def search(self, curr, node):
        """Finds And Returns Specific Node"""
        while curr.data != node.data:
            if curr.data < node.data:
                if curr.right is not None:
                    curr = curr.right
            else:
                if curr.left is not None:
                    curr = curr.left
        return curr


def sort(arr):
    """Sorting Function"""
    tree = BST()
    tree.insertRec(tree.root, Node(arr[0]))
    for item in arr:
        if item == tree.root.data:
            continue
        tree.insertRec(tree.root, Node(item))
    ret = []
    return treeSort(tree.root, ret)


def treeSort(root, ret):
    """Helper Function Building Sorted Array Recursively"""
    if root is None:
        return
    treeSort(root.left, ret)
    ret.append(root.data)
    treeSort(root.right, ret)
    return ret


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
recTree = BST()
recTree.insertRec(recTree.root, Node(50))
recTree.insertRec(recTree.root, Node(10))
recTree.insertRec(recTree.root, Node(75))
recTree.insertRec(recTree.root, Node(90))
recTree.insertRec(recTree.root, Node(15))
recTree.insertRec(recTree.root, Node(30))
recTree.insertRec(recTree.root, Node(66))
recTree.insertRec(recTree.root, Node(17))
recTree.insertRec(recTree.root, Node(400))
recTree.insertRec(recTree.root, Node(1))
recTree.insertRec(recTree.root, Node(60))
recTree.insertRec(recTree.root, Node(22))
recTree.insertRec(recTree.root, Node(67))
recTree.insertRec(recTree.root, Node(4))
recTree.insertRec(recTree.root, Node(450))
recTree.insertRec(recTree.root, Node(92))
recTree.insertRec(recTree.root, Node(6))
recTree.insertRec(recTree.root, Node(29))
recTree.display(recTree.root)
print("Recursively Found Min: {0}".format(recTree.findMinRec(recTree.root).data))
print("Recursively Found Max: {0}".format(recTree.findMaxRec(recTree.root).data))
print("Recursively Found Next: {0}".format(recTree.findNextRec(recTree.root, Node(66)).data))
print("Recursively Found Prev: {0}".format(recTree.findPrevRec(recTree.root, Node(29))))#.data))
recTree.deleteRec(recTree.root, Node(17))
recTree.deleteRec(recTree.root, Node(50))
recTree.deleteRec(recTree.root, Node(400))
recTree.deleteRec(recTree.root, Node(4))
print("BST After Recursively Deleting 17, 50, 400, and 4:")
recTree.display(recTree.root)

print("\n\nTest Iterative Functions")
iterTree = BST()
iterTree.insertIter(iterTree.root, Node(50))
iterTree.insertIter(iterTree.root, Node(10))
iterTree.insertIter(iterTree.root, Node(75))
iterTree.insertIter(iterTree.root, Node(90))
iterTree.insertIter(iterTree.root, Node(15))
iterTree.insertIter(iterTree.root, Node(30))
iterTree.insertIter(iterTree.root, Node(66))
iterTree.insertIter(iterTree.root, Node(17))
iterTree.insertIter(iterTree.root, Node(400))
iterTree.insertIter(iterTree.root, Node(1))
iterTree.insertIter(iterTree.root, Node(60))
iterTree.insertIter(iterTree.root, Node(22))
iterTree.insertIter(iterTree.root, Node(67))
iterTree.insertIter(iterTree.root, Node(4))
iterTree.insertIter(iterTree.root, Node(450))
iterTree.insertIter(iterTree.root, Node(92))
iterTree.insertIter(iterTree.root, Node(6))
iterTree.insertIter(iterTree.root, Node(29))
iterTree.display(iterTree.root)
print("Iteratively Found Min: {0}".format(iterTree.findMinIter(iterTree.root).data))
print("Iteratively Found Max: {0}".format(iterTree.findMaxIter(iterTree.root).data))
print("Iteratively Found Next: {0}".format(iterTree.findNextIter(iterTree.root, Node(66)).data))
print("Iteratively Found Prev: {0}".format(iterTree.findPrevIter(iterTree.root, Node(29)).data))
iterTree.deleteIter(iterTree.root, Node(17))
iterTree.deleteIter(iterTree.root, Node(50))
iterTree.deleteIter(iterTree.root, Node(400))
iterTree.deleteIter(iterTree.root, Node(4))
print("BST After Iteratively Deleting 17, 50, 400, and 4:")
iterTree.display(iterTree.root)

print("\n\nTest Question 2 & 3")
randomArr = getRandomArray(10)
print(randomArr)
sortedArr = sort(randomArr)
print(sortedArr)

print(getSortedArray(10))
