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



if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    print(tree.root.left,'************')
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())
    print(tree.contains(1))
    print(tree.contains(5))

    ## [2,1,4,3]