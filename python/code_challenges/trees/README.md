# Trees

* Node - A Tree node is a component which may contain it’s own values, and references to other nodes

* Root - The root is the node at the beginning of the tree

* K - A number that specifies the maximum number of children any node may have in a k-ary tree. In a binary tree, k = 2.

* Left - A reference to one child node, in a binary tree

* Right - A reference to the other child node, in a binary tree

* Edge - The edge in a tree is the link between a parent and child node

* Leaf - A leaf is a node that does not have any children

* Height - The height of a tree is the number of edges from the root to the furthest leaf

## Challenge

* Node

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

* Binary Tree

* Create a Binary Tree class

* Define a method for each of the depth first traversals:

* pre order

* in order

* post order which returns an array of the values, ordered appropriately.

* Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

* Binary Search Tree

* Create a Binary Search Tree class

* This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

* Add

* Arguments: value

* Return: nothing

* Adds a new node with that value in the correct location in the binary search tree.

* Contains

* Argument: value

* Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

Big O

pre order : 

time : O(n) 

space : O(n)

in order : 

time : O(n) 

space : O(n)

post order : 

time : O(n) 

space : O(n)

Add : 

time : O(n) 

space : O(1)

Contains : 

time : O(n) 

space : O(1)

## API

Pre-order: root >> left >> right

In-order: left >> root >> right

Post-order: left >> right >> root

add a new node with value 

contains Returns boolean if the value that sent within the function is exist or not 