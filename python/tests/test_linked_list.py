class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):
      
        # try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current
        # except Exception as error:
        #   raise Exception(f"Something Wrong : {error}")



    def includes(self,n):
        
        # try:
          result=False

          current = self.head
          while current:
              if current.value==n:

                  result=True
                  break
              current=current.next
          return result
        # except Exception as error:
        #   raise Exception(f"Something Wrong : {error}")

   


    def __str__(self):
        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += "( "+ str(value) +") => None "
                # output += f"( {value} ) => None"
                # print(output)
                break
            output = output +  "( "+ str(value) +") =>"
            # output = output + f"( {value} ) => "
            current=current.next
        return output

# import pytest
def test_empty_linkedList():
    lList = LinkedList()
    actual = lList.head
    assert actual == None

def test_insert():
    lList = LinkedList()
    lList.insert(6)
    lList.insert(8)
    actual= lList.head.value
    actualNone = lList.head.next.value
    excepted = 6
    print(actual)
    
    assert lList.head.value == 8
    assert actualNone == 6

def test_includes():
    lList=LinkedList()
    lList.insert(7)
    lList.insert(15)
    lList.insert(70)
    actual=lList.includes(70)
    excepted=True

    assert actual == excepted
    
def test_False_includes():
    lList=LinkedList()
    lList.insert(7)
    lList.insert(15)
    actual=lList.includes(70)
    excepted=False

    assert actual == excepted

def test_everyThing_print():
    lList=LinkedList()
    lList.insert(10)   
    lList.insert(20)    
    lList.insert(30)   
    lList.__str__()
    actual = '( 30) =>( 20) =>( 10) => None'
    excepted = '( 30) =>( 20) =>( 10) => None'

    assert actual == excepted