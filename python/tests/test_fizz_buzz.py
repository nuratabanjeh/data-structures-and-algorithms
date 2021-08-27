class Node:
    def __init__(self,value):
        self.value = value
        self.value = value
        self.children=[]
        # self.left = None
        # self.right = None
      

class k_arr_tree:
    def __init__(self):
        self.root=None


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

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front=node
            self.rear = node
        else:
            self.rear.next = node
            self.rear= node

    def dequeue(self):
        try:
            remove=self.front.value
            self.front=self.front.next
            return remove
        except: 
            return "empty"

    def peek(self):
        try:
            return self.front.value
        except:
            return("empty")

    def isEmpty(self):
        if (not self.rear and self.front) or (self.rear and not self.front):
          raise Exception("empty")
        return not self.rear




def fizz_Buzz_Tree(k_arr_tree): 

    def append_in_tree(node):
        if node.children : 
            for x in range(len(node.children)): 
                append_in_tree (node.children[x])

                
                if node.children[x].value %3 == 0 : 
                    node.children[x].value= "Fizz"
                elif node.children[x].value %5 == 0 : 
                    node.children[x].value= "Buzz"
                elif node.children[x].value %3 == 0 and node.children[x].value % 5 == 0:
                    node.children[x].value= "Fizz Buzz"
                else: node.children[x].value =str(node.children[x].value)
    append_in_tree(k_arr_tree.root)            
    if k_arr_tree.root.value %5 == 0 and k_arr_tree.root.value %3 ==0 : 
        k_arr_tree.root.value ="Fizz Buzz"
    if k_arr_tree.root.value %5 == 0 : 
        k_arr_tree.root.value ="Buzz"
    if k_arr_tree.root.value %3 ==0 : 
        k_arr_tree.root.value ="Fizz"
    else : 
        k_arr_tree.root.value= str(k_arr_tree.root.value)

    return k_arr_tree
######################test###########


def test_fizz_buzz():
    ktree = k_arr_tree()
  
    ktree.root=Node(17)
    ktree.root.children+=[Node(15)] 
    ktree.root.children+=[Node(5)]
    ktree.root.children+=[Node(9)]
    fizz_Buzz_Tree(ktree)
    actual = ktree.root.children[0].value
    excpected = "Fizz" 
    assert actual == excpected

def test_not_divisable_on_3_or_5():
    ktree = k_arr_tree()
  
    ktree.root=Node(17)
    ktree.root.children+=[Node(11)] 
    ktree.root.children+=[Node(5)]
    ktree.root.children+=[Node(9)]
    fizz_Buzz_Tree(ktree)
    actual = ktree.root.children[0].value
    excpected = "11" 
    assert actual == excpected

