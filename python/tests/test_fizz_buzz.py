class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
      

class BinaryTree:
    def __init__(self):
        self.root = None

## i useded recursive function(call back function)

    def pre_order(self):
        treeList=[]
        def _pre_order(root):
            if not root:
                return
            treeList.append(root.value)
            if root.left:
                _pre_order(root.left)
            if root.right:
                _pre_order(root.right)
        
        _pre_order(self.root)
        return treeList
            

    def in_order(self):
        treeList=[]
        def _in_order(root):
            if not root:
                return

            if root.left:
                _in_order(root.left)
            treeList.append(root.value)
            if root.right:
                _in_order(root.right)
        _in_order(self.root)
        return treeList


    def post_order(self):
        treeList=[]
        def _post_order(root):
            if not root:
                return
            if root.left:
                _post_order(root.left)
            if root.right:
                _post_order(root.right)

            treeList.append(root.value)
        _post_order(self.root)
        return treeList

        

# class K_Arr_Tree:
#     def __init__(self):
#         self.root = None

def fizz_buzz(x):
    if type(x)is not int :
        return x
    elif x % 3 == 0 and x %5 == 0 :
        return "FizzBuzz"

    elif x % 3 == 0 :
        return "Fizz"

    elif x % 5 == 0 :
        return "Buzz"

    else:
        return str(x)

def fizz_buzz_tree(k_array_tree):
    new_tree = k_array_tree
    def _pre_order(root):
            if not root:
             return
            new_value = fizz_buzz(root.value)  
            root.value = new_value
           
            if root.left:
                _pre_order(root.left)
            if root.right:
                _pre_order(root.right)
        
    _pre_order(new_tree.root)
    return new_tree

######################test###########


def test_fizz_buzz():
  tree = BinaryTree()
  tree.root = Node(17)
  tree.root.left = Node(15)
  tree.root.right = Node(5)
  tree.root.right.left = Node(9)
  newTree=fizz_buzz_tree(tree)
  actual = newTree.root.left.value
  excpected = "FizzBuzz" 
  assert actual == excpected

def test_expected_faliure():
  tree = BinaryTree()
  tree.root = Node('nura')
  newTree=fizz_buzz_tree(tree)
  actual = newTree.root.value
  excpected = "nura" 
  assert actual == excpected
