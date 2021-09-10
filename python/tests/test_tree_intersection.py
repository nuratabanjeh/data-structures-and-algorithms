import pytest
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root=None):
        self.root = root

# i useded recursive function(call back function)

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

class LinkedList:
  def __init__(self):
    self.head = None


  def includes(self,vlaue):
      current=self.head
      while current :
          if vlaue ==current.value[0]:
              return True
          current=current.next
      return False

  def append(self,value):
      new_node=Node(value)

      if self.head == None:
          self.head = new_node
      else:
          current=self.head
          while current.next:
              current=current.next
          current.next=new_node

class Hashtable:
  def __init__(self, size = 1024):
      self.size = size
      self._buckets = [None]*size 
    
  def hash(self,key):
    value=0
    for x in key:
      value += ord(x)
    index = (value * 7) % self.size   
    return index
    
  def add(self,key,value):
    '''add a value to the hashtable by its key 
    parameters:
        key: a string
        value: any type
    Arrgument: key and value 
    return: nothing

    '''
    index = self.hash(key) 

    if not self._buckets[index]:
      self._buckets[index] = LinkedList()
      

    self._buckets[index].append([key,value])

  def contains(self,key):
    """this function will check if the there is a value for the key 
    parameters:
      key: a string
    return: a boolean
    """
    index=self.hash(key)
    if self._buckets[index]:
      return self._buckets[index].includes(key)
    else:
      return False

  def get(self,key):

      index = self.hash(key)
      if self._buckets[index] == None:
          return None
      else:
          current=self._buckets[index].head
          while current:
              if current.value[0] == key:
                  return current.value[1]
              current = current.next


def tree_intersection(first_tree,second_tree):
    tree_hash = add_tree_to_hashmap(first_tree)

    new_list = []
    def add_common_to_list(node):
        str_value = str(node.value)
        if tree_hash.contains(str_value):
            new_list.append(node.value)

        if node.left:
            add_common_to_list(node.left)

        if node.right:
            add_common_to_list(node.right)

    if second_tree.root:
        add_common_to_list(second_tree.root)
    return new_list


def add_tree_to_hashmap(tree):
    hashmap = Hashtable()
    def walk(node):
        str_value = str(node.value)
        hashmap.add(str_value, 1)

        if node.left:
            walk(node.left)

        if node.right:
            walk(node.right)

    if tree.root:
        walk(tree.root)
    return hashmap



######################TEST###################

def test_tree_intersection():
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
    
    actual=tree_intersection(binary_first_tree, binary_second_tree)
    expected=[100, 160, 125, 175, 200, 350, 500]
    assert actual == expected

def test_no_intersection():
    first_tree = Node(15)
    first_tree.left = Node(10)
    first_tree.left.left = Node(7)
    first_tree.left.right = Node(16)
    first_tree.right = Node(25)
    first_tree.right.left = Node(20)
    first_tree.right.right = Node(35)
    binary_first_tree = BinaryTree(first_tree)
    second_tree = Node(42)
    second_tree.left = Node(8)
    second_tree.left.left = Node(6)
    second_tree.left.right = Node(18)
    second_tree.right = Node(33)
    second_tree.right.left = Node(29)
    second_tree.right.right = Node(34)
    binary_second_tree = BinaryTree(second_tree)    
    actual = tree_intersection(binary_first_tree, binary_second_tree)
    expected=[]
    assert actual == expected

