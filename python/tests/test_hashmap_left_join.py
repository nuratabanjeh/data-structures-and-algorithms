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
    index = self.hash(key) 

    if not self._buckets[index]:
      self._buckets[index] = LinkedList()
      

    self._buckets[index].append([key,value])

  def contains(self,key):
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


def left_join(first_hash_table,second_hash_table):
    output_array=[]
    if first_hash_table._buckets == first_hash_table.size*[None] or second_hash_table._buckets == second_hash_table.size*[None] :
        return 'Empty'
    for word in first_hash_table._buckets:
        if word:
            arr2=[]
            arr2.append(word.head.value[0])
            arr2.append(first_hash_table.get(word.head.value[0]))
            arr2.append(second_hash_table.get(word.head.value[0]))
            output_array.append(arr2)
    return output_array

##########TEST############

def test_left_join():
    first_hash_table = Hashtable()
    first_hash_table.add('fond', 'enamored')
    first_hash_table.add('wrath', 'anger')
    first_hash_table.add('diligent', 'employed')
    first_hash_table.add('outfit', 'grap')
    first_hash_table.add('guide', 'usher')
    second_hash_table = Hashtable()
    second_hash_table.add('fond', 'averse')
    second_hash_table.add('wrath', 'delight')
    second_hash_table.add('diligent', 'idle')
    second_hash_table.add('guide', 'follow')
    second_hash_table.add('flow', 'jam')
    actual= left_join(first_hash_table,second_hash_table)
    expected= [['outfit', 'grap', None], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]
    assert actual == expected

def test_empty_hashtable():
    first_hash_table = Hashtable()
    second_hash_table = Hashtable()
    second_hash_table.add('fond', 'averse')
    second_hash_table.add('wrath', 'delight')
    second_hash_table.add('diligent', 'idle')
    second_hash_table.add('guide', 'follow')
    second_hash_table.add('flow', 'jam')
    actual= left_join(first_hash_table,second_hash_table)
    expected= 'Empty'
    assert actual == expected