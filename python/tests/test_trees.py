class Node:
    def __init__(self, value):
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

    
    def tree_max(self):
        if not self.root:
            return "No tree"
    
        treeList = self.pre_order()
        print(treeList)
        max=0
        for value in treeList:

            if max < value :
                max = value 
        
        return max



class BinarySearchTree(BinaryTree):
    def add(self,value):
        
        addingNode = Node(value)
        currentNode = self.root
        if addingNode.value == currentNode:
            return "the value must be unique"
        if not self.root:
            self.root = addingNode
        else:
            def _add(addingNode , currentNode ):
                while currentNode.value != addingNode.value:
                    if addingNode.value < currentNode.value:
                        if not currentNode.left:
                            currentNode.left = addingNode
                            return
                        else:
                            currentNode == currentNode.left 
                            _add(addingNode,currentNode)
                    else:
                        if not currentNode.right :
                            currentNode.right = addingNode
                            return
                        else:
                            currentNode = currentNode.right
                            _add(addingNode,currentNode)


            _add(addingNode,currentNode)




        

    
    def contains(self,value):
        currentNode=self.root
        while currentNode:
            if currentNode.value == value:
                 return True
            if currentNode.value > value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        
        return False
###########testsss##########

def test_empty_tree():
    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_single_root():
    tree = BinarySearchTree()
    tree.add(1)
    
    actual = tree.root.value
    excepted = 1 
    assert actual == excepted

def test_add_left_and_right():
    tree=BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    actualRight = tree.root.right.value
    actualLeft = tree.root.left
    expectedRight = 2
    expectedLeft = None
    assert actualRight == expectedRight 
    assert actualLeft == expectedLeft 

def test_preOrder():
    tree=BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    actual = tree.pre_order()
    expected = [1, 2, 3, 4]
    assert actual == expected

def test_inOrder():
    tree=BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    actual = tree.in_order()
    expected = [1, 2, 3, 4]
    assert actual == expected

def test_postOrder():
    tree=BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    actual = tree.post_order()
    expected = [4, 3, 2, 1]
    assert actual == expected


def test_happyPath():
    treeSearch = BinarySearchTree()
    treeSearch.add(1)
    treeSearch.add(2)
    treeSearch.add(3)
    treeSearch.add(40)
    actual = treeSearch.tree_max()
    expected = 40
    assert actual == expected 

def test_expectedFaliure():
    treeSearch = BinarySearchTree()
    actual = treeSearch.tree_max()
    expected = "No tree"
    assert actual == expected 




