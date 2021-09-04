class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)
  def insert(self, value):
    node = Node(value)
    if self.head:
        node.next = self.head
    self.head = node   


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
    

######Test####



def test_add():
    test=Hashtable()
    test.add('Nura',25)
    assert test.contains('Nura')==True

def test_null_for_key_not_exist():
    test = Hashtable()
    test=test.get('Nura')
    expected=None
    assert test==expected

def test_collision():
    test = Hashtable()
    test.add('Nura', 96)
    test.add('mhmoud', 90)
    assert test.get('Nura') == 96

def test_retrieve_value_from_hashtable():
    test = Hashtable()
    test.add('Nura', 96)
    test.add('Mhmoud', 93)
    assert (test.get('Nura') == 96 and test.get('Mhmoud')== 93)