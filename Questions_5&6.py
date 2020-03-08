# Jonathan Nunes
# Project 1: Questions 5 & 6

import random


AVLctr = 0
BSTctr = 0


class AVLNode:
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
        global AVLctr

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
                    AVLctr += 1
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
                    AVLctr += 1

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
        global AVLctr

        while curr.left is not None:
            curr = curr.left  # Finding the leftmost node
            AVLctr += 1
        return curr

    def findMaxIter(self, curr):
        """Iterative Find Max"""
        global AVLctr

        while curr.right is not None:
            curr = curr.right  # finding the rightmost node
            AVLctr += 1
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


class BSTNode:
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
        # Insertion on empty tree
        if self.root is None:
            self.root = node
        else:
            # If node to be inserted is greater than current node
            if curr.data < node.data:
                if curr.right is None:
                    curr.right = node  # Inserting node to right child
                    curr.right.parent = curr  # Marking current as parent
                else:
                    self.insertRec(curr.right, node)
            else:
                # If node to be inserted is less than current node
                if curr.left is None:
                    curr.left = node  # Inserting node to left child
                    curr.left.parent = curr  # Marking current as parent
                else:
                    self.insertRec(curr.left, node)

    def deleteRec(self, curr, node):
        """Recursive Deletion"""
        # Base case
        if curr is None:
            return curr

        # Finding node to delete within tree
        if curr.data > node.data:
            curr.left = self.deleteRec(curr.left, node)
        elif curr.data < node.data:
            curr.right = self.deleteRec(curr.right, node)
        else:

            # Deleting "node" and reassigning child/parent connections
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
        # Finding the node within the tree
        curr = self.search(self.root, node)

        # Base case
        if curr is None:
            return curr
        # If a right child exists it'll be the smallest value
        if curr.right is not None:
            return self.findMinRec(curr.right)
        # If no right child exists, go up the parent until you find a right child
        if curr.parent.left.data == curr.data:
            return curr.parent
        # else:

    def findPrevRec(self, curr, node):
        """Recursive Find Prev"""
        pass

    def findMinRec(self, curr):
        """Recursive Find Min"""
        if curr.left is not None:
            return self.findMinRec(curr.left)  # Finding the left most node
        else:
            return curr

    def findMaxRec(self, curr):
        """Recursive Find Max"""
        if curr.right is not None:
            return self.findMaxRec(curr.right)  # Finding the right most node
        else:
            return curr

    def insertIter(self, curr, node):
        """Iterative Insertion"""
        global BSTctr

        # Insertion into empty tree
        if self.root is None:
            self.root = node
            return
        # While it hasn't inserted
        while True:
            if curr.data < node.data:
                if curr.right is None:
                    curr.right = node  # Inserting node to right child
                    curr.right.parent = curr  # marking current as parent
                    break
                else:
                    curr = curr.right
                    BSTctr += 1
            else:
                if curr.left is None:
                    curr.left = node  # Inserting node to left child
                    curr.left.parent = curr  # marking current as parent
                    break
                else:
                    curr = curr.left
                    BSTctr += 1

    def deleteIter(self, curr, node):
        """Iterative Deletion"""
        pass

    def findNextIter(self, curr, node):
        """Iterative Find Next"""
        # Search for node in tree
        curr = self.search(self.root, node)

        ##If a right child exists it'll be the smallest value
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
        global BSTctr

        while curr.left is not None:
            curr = curr.left  # Finding the leftmost node
            BSTctr += 1
        return curr

    def findMaxIter(self, curr):
        """Iterative Find Max"""
        global BSTctr

        while curr.right is not None:
            curr = curr.right  # finding the rightmost node
            BSTctr += 1
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


def BSTsort_Rec(arr):
    """Sorting Function"""
    tree = BST()

    # insert root
    tree.insertRec(tree.root, BSTNode(arr[0]))

    # for every item, insert into tree
    for item in arr:
        if item == tree.root.data:
            continue
        tree.insertRec(tree.root, BSTNode(item))
    ret = []

    # i needed a helper for the sorting
    return treeSort(tree.root, ret)


def treeSort(root, ret):
    """Helper Function Building Sorted Array Recursively"""
    #An in order traversal
    if root is None:
        return
    treeSort(root.left, ret)
    ret.append(root.data)
    treeSort(root.right, ret)
    return ret


def BSTsort_Iter(arr):
    """Sorting Function"""
    tree = BST()

    # insert root
    tree.insertIter(tree.root, BSTNode(arr[0]))

    # for every item, insert into tree
    for item in arr:
        if item == tree.root.data:
            continue
        tree.insertIter(tree.root, BSTNode(item))
    ret = []

    node = tree.findMinIter(tree.root).data
    ret.append(node)
    while tree.findNextIter(tree.root, BSTNode(node)) is not None:
        ret.append(tree.findNextIter(tree.root, BSTNode(node)).data)
        node = tree.findNextIter(tree.root, BSTNode(node)).data

    return ret


def AVLsort_Iter(arr):
    """Sorting Function"""
    tree = AVL()

    # insert root
    tree.insertIter(tree.root, AVLNode(arr[0]))

    # for every item, insert into tree
    for item in arr:
        if item == tree.root.data:
            continue
        tree.insertIter(tree.root, AVLNode(item))
    ret = []

    node = tree.findMinIter(tree.root).data
    ret.append(node)
    while tree.findNextIter(tree.root, AVLNode(node)) is not None:
        ret.append(tree.findNextIter(tree.root, AVLNode(node)).data)
        node = tree.findNextIter(tree.root, AVLNode(node)).data

    return ret


def getRandomArray(n):
    """Create Randomly Filled Array"""
    temp = random.randint(1, n)
    arr = [None] * n
    for i in range(n):
        while temp in arr:
            temp = random.randint(1, n + 1)  # adding n items between 0-999 to return array
        arr[i] = temp
    return arr


def getSortedArray(n):
    """Created Sorted Array"""
    arr = [None] * n
    for i in range(n):
        arr[i] = n - i  # Using the negative indexing to insert into return array
    return arr


print("Testing And Answering Questions")
unsorted = getRandomArray(10000)
issorted = getSortedArray(10000)

fiveA = BSTsort_Rec(unsorted)
print("5(a)\nBST Recursive:", fiveA)

fiveC_BST = BSTsort_Iter(unsorted)
print("\n5(c)\nBST Iteration:", fiveC_BST)
#fiveC_AVL = AVLsort_Iter(unsorted)  # Not working, i think this is where my rotation edge case is problematic
print("\nAVL Iteration: Can't Figure Out Edge Case") #, fiveC_AVL)

print("\n6(b)\nBST Traversals: {0}\tAVL Traversals: {1}".format(BSTctr, AVLctr))

AVLctr = 0
BSTctr = 0

sixC_BST = BSTsort_Iter(issorted)
print("\n6(c)\nBST Iteration:", sixC_BST)
sixC_AVL = AVLsort_Iter(issorted)  # Not working
print("\nAVL Iteration:", sixC_AVL)

print("\n6(c)\nBST Traversals: {0}\tAVL Traversals: {1}".format(BSTctr, AVLctr))
