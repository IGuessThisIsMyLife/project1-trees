# project1-trees
CS 435 - Project 1: Trees
Part 1 Questions i handed in in class.

Part 2 Questions:
4(a)
Properties:
  1. Node has no more than two children
  2. Left subtree are all values less than the parent node
  3. Right subtree are all values greater than the parent node
  4. The heights of the left and right subtrees can't have an absolute difference greater 

(b)
insert - O(n) because of the addition of the rebalancing

delete - O(n) because of the addition of the rebalancing

find-next - O(log n) because since the tree should be balanced, it will only ever need to traverse exponentially half the tree

find-prev - O(log n) because since the tree should be balanced, it will only ever need to traverse exponentially half the tree

find-min - O(log n) because since the tree should be balanced, it will only ever need to traverse exponentially half the tree

find-max - O(log n) becasue since the tree should be balanced, it will only ever need to traverse exponentially half the tree
