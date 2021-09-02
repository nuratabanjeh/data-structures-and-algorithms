


class Node:
  ''''
  THis the class is responsiple to create the Nodes 
  '''
  def __init__(self, value=""):
    self.value = value
    self.next = None

  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)


class LinkedList():
  
  '''
  This Class Responsable For Creating LinkdeList 
  '''
  def __init__(self):
    self.head = None

  def insert(self, value):
    node = Node(value)
    # print(node)
    if self.head:
      node.next = self.head

    self.head = node

  def includes(self,vlaue):
     current=self.head
     while current :
        #  print(current.value)
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


class HashTable :

  def __init__(self, size = 1024):
    
    self.size = size
    self._buckets = [None] *self.size



  def hash(self,key:str)->int:
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
    # index =self.hash(key)
    # if not self._buckets[index]:
    #   self._buckets[index]=[[key,value]]
    # else:
    #   self._buckets[index].append([key,value])

    index = self.hash(key) 

    if not self._buckets[index]:
      self._buckets[index] = LinkedList()
      

    self._buckets[index].append([key,value])



  def find(self,key):
    """this function will search in the hashtable about the key and return the value
    parameters:
      key: a string
    return: the value 
      """
    index = self.hash[key]
    return index
    

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
    

######Test####


def test_add():
  test=HashTable()
  test.add('ahmad',555)
  assert test.contains('ahmad')==True 