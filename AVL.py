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
        self.bf = 0


class AVL:
    def __init__(self):
        """Balanced Binary Search Tree Constructor"""
        self.root = None


    def findMinRec(self, curr):
        """Recursive Find Min"""
        if curr.left is not None:
            return self.findMinRec(curr.left) #Just finding the left most node
        else:
            return curr


    def findMaxRec(self, curr):
        """Recursive Find Max"""
        if curr.right is not None:
            return self.findMaxRec(curr.right) #Just finding the right most node
        else:        
            return curr  


    def insertIter(self, curr, node):
        """Iterative Insertion"""
        #Im struggling incorporating the balance factor and I felt like i got close
        if self.root is None:
            self.root = node
            return
        while True:
            if curr.data < node.data:
                if curr.right is None:
                    curr.right = node
                    curr.right.parent = curr
                    curr.bf-=1              #This almost works
                    self.updateBFs(curr)    #but there's an edge case somewhere
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                    curr.left.parent = curr
                    curr.bf+=1              #same here
                    self.updateBFs(curr)
                    break
                else:
                    curr = curr.left
        #self.checkBalances(self.root)      #Trying to get this to be my savior


    def deleteIter(self, curr, node):
        """Iterative Deletion"""
        pass


    def findNextIter(self, curr, node):
        """Iterative Find Next"""
        #Search for node in tree
        curr = self.search(self.root, node)
        #If a right child exists it'll be the smallest value
        if curr.right is not None:
            return self.findMinIter(curr.right)
        #If no right child exists, go up the parent until you find a right child
        parent = curr.parent
        while parent is not None:
            if curr != parent.right:
                break
            curr = parent
            parent = parent.parent
        return parent


    def findPrevIter(self, curr, node):
        """Iterative Find Prev"""
        #Search for node in tree
        curr = self.search(self.root, node)
        #If a left child exists it'll be the smallest value
        if curr.left is not None:
            return self.findMaxIter(curr.left)
        #If no left child exists, go up the parent until you find a left child
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
            curr = curr.left    #Finding the leftmost node
        return curr


    def findMaxIter(self, curr):
        """Iterative Find Max"""
        while curr.right is not None:
            curr = curr.right   #finding the rightmost node
        return curr


    def updateBFs(self, curr):
        """Goes Up Each Parent, Updating The Balance Factors"""
        #Iteratively goes up the parents determining balance factors
        while curr is not None and curr.parent is not None:
            if curr.parent.right is not None and curr.data == curr.parent.right.data:
                curr.parent.bf-=1   #subtracting if node was inserted from right
            elif curr.parent.left is not None and curr.data == curr.parent.left.data:
                curr.parent.bf+=1   #adding if node was inserted from left
            curr = curr.parent


    def checkBalances(self, curr):
        """Checks Tree's Balance And Rotates Accordingly"""
        #Still trying to piece this together properly for all the cases
        if curr.bf > 1:
            return self.rotateRight(curr)

        if curr.bf < -1:
            return self.rotateLeft(curr)

        if curr.bf > 1:
            curr.left = self.rotateLeft(curr.left)
            return self.rotateRight(curr)

        if curr.bf < -1:
            curr.right = self.rotateRight(curr.right)
            return self.rotateLeft(curr)

        return curr


    def rotateLeft(self, pivot):
        """Rotates To The Left"""
        pass


    def rotateRight(self, pivot):
        """Rotates To The Right"""
        pass

    
    def display(self, curr):
        """For My Testing Purposes: Prints All Nodes In Order"""
        if curr is None:
            return
        self.display(curr.left)
        if curr.parent is None:
            print("Node: {0}, BF: {1}, Parent: {2}".format(curr.data, curr.bf, "Root"))
        else:
            print("Node: {0}, BF: {1}, Parent: {2}".format(curr.data, curr.bf, curr.parent.data))
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
