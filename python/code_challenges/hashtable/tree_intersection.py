class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root=None):
        self.root = root

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


def tree_intersection(first_tree,second_tree):
  outPut_array=[]
  if first_tree.root == None or second_tree.root == None:
    return None
  def check_equality(root1,root2):
    if root1.value == root2.value:
      outPut_array.append(root1.value)
    if root1.left and root2.left:
      check_equality(root1.left ,root2.left)
    if root1.right and root2.right :
      check_equality(root1.right ,root2.right)
  check_equality(first_tree.root,second_tree.root)
  return outPut_array


if __name__=="__main__":
  first_tree = Node(150)
  first_tree.left = Node(100)
  first_tree.left.left = Node(75)
  first_tree.left.right = Node(160)
  first_tree.left.right.left = Node(125)
  first_tree.left.right.right = Node(175)
  first_tree.right = Node(250)
  first_tree.right.left = Node(200)
  first_tree.right.right = Node(350)
  first_tree.right.right.left = Node(300)
  first_tree.right.right.right = Node(500)
  binary_first_tree = BinaryTree(first_tree)

  print(binary_first_tree.pre_order())


  second_tree = Node(42)
  second_tree.left = Node(100)
  second_tree.left.left = Node(15)
  second_tree.left.right = Node(160)
  second_tree.left.right.left = Node(125)
  second_tree.left.right.right = Node(175)
  second_tree.right = Node(600)
  second_tree.right.left = Node(200)
  second_tree.right.right = Node(350)
  second_tree.right.right.left = Node(4)
  second_tree.right.right.right = Node(500)
  binary_second_tree = BinaryTree(second_tree)

  print(binary_second_tree.pre_order())
  
  print(tree_intersection(binary_first_tree, binary_second_tree))
  
#############################################
  first_tree = Node(15)
  first_tree.left = Node(10)
  first_tree.left.left = Node(7)
  first_tree.left.right = Node(16)
  first_tree.right = Node(25)
  first_tree.right.left = Node(20)
  first_tree.right.right = Node(35)
  binary_first_tree = BinaryTree(first_tree)

  print(binary_first_tree.pre_order())


  second_tree = Node(42)
  second_tree.left = Node(8)
  second_tree.left.left = Node(6)
  second_tree.left.right = Node(18)
  second_tree.right = Node(33)
  second_tree.right.left = Node(29)
  second_tree.right.right = Node(34)
  binary_second_tree = BinaryTree(second_tree)

  print(binary_second_tree.pre_order())
  
  print(tree_intersection(binary_first_tree, binary_second_tree))

