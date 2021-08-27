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

    def re_value(node):
        if node.children : 
            for x in range(len(node.children)): 
                re_value (node.children[x])

                
                if node.children[x].value %3 == 0 : 
                    node.children[x].value= "Fizz"
                elif node.children[x].value %5 == 0 : 
                    node.children[x].value= "Buzz"
                elif node.children[x].value %3 == 0 and node.children[x].value % 5 == 0:
                    node.children[x].value= "Fizz Buzz"
                else: node.children[x].value =str(node.children[x].value)
    re_value(k_arr_tree.root) 
            
    if k_arr_tree.root.value %5 == 0 and k_arr_tree.root.value %3 ==0 : 
        k_arr_tree.root.value ="Fizz Buzz"
    if k_arr_tree.root.value %5 == 0 : 
        k_arr_tree.root.value ="Buzz"
    if k_arr_tree.root.value %3 ==0 : 
        k_arr_tree.root.value ="Fizz"
    else : 
        k_arr_tree.root.value= str(k_arr_tree.root.value)

    return k_arr_tree
# def fizz_buzz(x):
#     if type(x)is not int :
#         return x
#     elif x % 3 == 0 and x %5 == 0 :
#         return "FizzBuzz"

#     elif x % 3 == 0 :
#         return "Fizz"

#     elif x % 5 == 0 :
#         return "Buzz"

#     else:
#         return str(x)
        

# def fizz_buzz_tree(k_array_tree):
#     new_tree = k_array_tree
#     def _pre_order(root):
#             if not root:
#              return
#             new_value = fizz_buzz(root.value)  
#             root.value = new_value
           
#             if root.left:
#                 _pre_order(root.left)
#             if root.right:
#                 _pre_order(root.right)
        
#     _pre_order(new_tree.root)
#     return new_tree


if __name__ == '__main__':
    
#   tree = BinaryTree()
#   tree.root = Node(17)
#   tree.root.left = Node(15)
#   tree.root.right = Node(9)
#   tree.root.right.left = Node(9)
#   fizz_buzz_tree = fizz_buzz_tree(tree)
#   print(fizz_buzz_tree.root.right.value)
    ktree = k_arr_tree()
    ktree.root=Node(17)
    ktree.root.children+=[Node(15)] 
    ktree.root.children+=[Node(5)]
    ktree.root.children+=[Node(9)]
    # ktree.root.children+=[Node(11)]

    print(fizz_Buzz_Tree(ktree))
    print(ktree.root.children[0].value)
    # print(ktree.root.children[0].value) 
    # print(ktree.root.children[3].value)

