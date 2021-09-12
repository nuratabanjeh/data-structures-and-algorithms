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
    
    def breadth_first(tree):
        theTree = [tree.root]
        breadthList = []
        if tree.root == None:
            return 'empty'
        while theTree:
            node = theTree[0]
            if node.left != None:
                theTree += [node.left]

            if node.right != None:
                    theTree+=[node.right]

            breadthList +=[theTree[0].value]
            theTree=theTree[1:]
        return breadthList

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root= Node(5)
    tree.root.left= Node(8)
    tree.root.right= Node(9)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(3)
    tree.root.left.right.left = Node(10)
    tree.root.left.right.right = Node(15)
    tree.root.right.right = Node(6)
    tree.root.right.right.left = Node(7)
    
    print(tree.breadth_first())
    