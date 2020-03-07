# Jonathan Nunes
# Project 1 (Part 2): AVL Tree

import random


class Node:
    def __init__(self, n):
        """Node Constructor"""
        self.left = None
        self.right = None
        self.data = n
        self.parent = None
        self.height = 1


class AVL:
    def __init__(self):
        """Balanced Binary Search Tree Constructor"""
        self.root = None

    def findMinRec(self, curr):
        """Recursive Find Min"""
        if curr.left is not None:
            return self.findMinRec(curr.left)  # Just finding the left most node
        else:
            return curr

    def findMaxRec(self, curr):
        """Recursive Find Max"""
        if curr.right is not None:
            return self.findMaxRec(curr.right)  # Just finding the right most node
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
                    curr.right = node  # Assign node
                    curr.right.parent = curr  # Assign node's parent
                    if curr.left is None:
                        lheight = 0
                    else:
                        lheight = curr.left.height
                    curr.height = 1 + max(lheight, curr.right.height)
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                    curr.left.parent = curr
                    if curr.right is None:
                        rheight = 0
                    else:
                        rheight = curr.right.height
                    curr.height = 1 + max(rheight, curr.left.height)
                    break
                else:
                    curr = curr.left

        self.updateHeights(curr)  # Iteratively update ancestry's heights
        while curr.parent is not None:
            balance = self.getBalance(curr)  # Obtain Balance Factor

            # Left Left Case
            if balance > 1 and node.data < curr.left.data:
                self.rotateRight(curr)
                break

            # Right Right Case
            if balance < -1 and node.data > curr.right.data:
                self.rotateLeft(curr)
                break

            # Left Right Case
            if balance > 1 and node.data > curr.left.data:
                self.rotateLeft(curr.left)
                self.rotateRight(curr)
                break

            # Right Left Case
            if balance < -1 and node.data < curr.right.data:
                self.rotateRight(curr.right)
                self.rotateLeft(curr)
                break
            curr = curr.parent

    def deleteIter(self, curr, node):
        """Iterative Deletion"""
        pass

    def findNextIter(self, curr, node):
        """Iterative Find Next"""
        # Search for node in tree
        curr = self.search(self.root, node)
        # If a right child exists it'll be the smallest value
        if curr.right is not None:
            return self.findMinIter(curr.right)
        # If no right child exists, go up the parent until you find a right child
        parent = curr.parent
        while parent is not None:
            if curr != parent.right:
                break
            curr = parent
            parent = parent.parent
        return parent

    def findPrevIter(self, curr, node):
        """Iterative Find Prev"""
        # Search for node in tree
        curr = self.search(self.root, node)
        # If a left child exists it'll be the smallest value
        if curr.left is not None:
            return self.findMaxIter(curr.left)
        # If no left child exists, go up the parent until you find a left child
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
            curr = curr.left  # Finding the leftmost node
        return curr

    def findMaxIter(self, curr):
        """Iterative Find Max"""
        while curr.right is not None:
            curr = curr.right  # finding the rightmost node
        return curr

    def updateHeights(self, curr):
        """Goes Up Each Parent, Updating The Balance Factors"""
        # Iteratively goes up the parents determining heights
        while curr is not None and curr.parent is not None:
            if curr.parent.left is None:
                lheight = 0
            else:
                lheight = curr.parent.left.height
            if curr.parent.right is None:
                rheight = 0
            else:
                rheight = curr.parent.right.height
            curr.parent.height = 1 + max(lheight, rheight)
            curr = curr.parent

    def getBalance(self, curr):
        """Checks Tree's Balance And Rotates Accordingly"""
        if curr.left is None:
            lheight = 0
        else:
            lheight = curr.left.height
        if curr.right is None:
            rheight = 0
        else:
            rheight = curr.right.height
        return lheight - rheight

    def rotateLeft(self, pivot):
        """Rotates To The Left"""
        mid = pivot.right
        if pivot.parent is not None:
            mid.parent = pivot.parent

            if mid.parent.left is None:
                mid.parent.right = mid
            elif mid.parent.right is None:
                mid.parent.left = mid
            else:
                if mid.parent.left.data == pivot.data:
                    mid.parent.left = mid
                else:
                    mid.parent.right = mid
        else:
            self.root = mid
            mid.parent = None

        if mid.left is not None:
            sub = mid.left
            pivot.right = sub
            sub.parent = pivot
        else:
            pivot.right = None

        mid.left = pivot
        pivot.parent = mid

        if pivot.left is None:
            lheight = 0
        else:
            lheight = pivot.left.height
        if pivot.right is None:
            rheight = 0
        else:
            rheight = pivot.right.height
        pivot.height = 1 + max(lheight, rheight)

        if mid.left is None:
            lheight = 0
        else:
            lheight = mid.left.height
        if mid.right is None:
            rheight = 0
        else:
            rheight = mid.right.height
        mid.height = 1 + max(lheight, rheight)

    def rotateRight(self, pivot):
        """Rotates To The Right"""
        mid = pivot.left
        if pivot.parent is not None:
            mid.parent = pivot.parent

            if mid.parent.left is None:
                mid.parent.right = mid
            elif mid.parent.right is None:
                mid.parent.left = mid
            else:
                if mid.parent.left.data == pivot.data:
                    mid.parent.left = mid
                else:
                    mid.parent.right = mid
        else:
            self.root = mid
            mid.parent = None

        if mid.right is not None:
            sub = mid.right
            pivot.left = sub
            sub.parent = pivot
        else:
            pivot.left = None

        mid.right = pivot
        pivot.parent = mid

        if mid.left is None:
            lheight = 0
        else:
            lheight = mid.left.height
        if mid.right is None:
            rheight = 0
        else:
            rheight = mid.right.height
        mid.height = 1 + max(lheight, rheight)

        if pivot.left is None:
            lheight = 0
        else:
            lheight = pivot.left.height
        if pivot.right is None:
            rheight = 0
        else:
            rheight = pivot.right.height
        pivot.height = 1 + max(lheight, rheight)

    def display(self, curr):
        """For My Testing Purposes: Prints All Nodes In Order"""
        if curr is None:
            return
        self.display(curr.left)
        print("Node: {0}, Height: {1}, Parent: {2}, Left Child: {3}, Right Child: {4}".format(curr.data, curr.height, "Root" if curr.parent is None else curr.parent.data, curr.left.data if curr.left is not None else None, curr.right.data if curr.right is not None else None))
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
    tree = AVL()

    # insert root
    tree.insertIter(tree.root, Node(arr[0]))

    # for every item, insert into tree
    for item in arr:
        if item == tree.root.data:
            continue
        tree.insertIter(tree.root, Node(item))
    ret = []

    node = tree.findMaxIter(tree.root).data
    num = 0
    ret[num] = node
    while tree.findNextIter(tree.root, Node(node)) is not None:
        ret[num + 1] = tree.findNextIter(tree.root, Node(node)).data
        node = tree.findNextIter(tree.root, Node(node)).data

    return ret


def getRandomArray(n):
    """Create Randomly Filled Array"""
    temp = random.randint(0, 99999)
    arr = [None] * n
    for i in range(n):
        while temp in arr:
            temp = random.randint(0, 99999)  # adding n items between 0-999 to return array
        arr[i] = temp
    return arr


def getSortedArray(n):
    """Created Sorted Array"""
    arr = [None] * n
    for i in range(n):
        arr[i] = n - i  # Using the negative indexing to insert into return array
    return arr

print("Test Iterative Functions")
iterTree = AVL()
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
print("AVL After Iteratively Deleting 17, 50, 400, and 4:")
iterTree.display(iterTree.root)
