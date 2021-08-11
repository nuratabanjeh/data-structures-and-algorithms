
class Node:
    def __init__(self, value= None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):
      
        try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current
        except Exception as error:
          raise Exception(f"Something Wrong : {error}")
    def append(self, value='null'):
    
        try:
            print(self, '******************55555')
            node = Node(value)
            if not self.head:
                self.head = node
            else:
                print('********',self)

                current=self.head
                while current.next != None:
                  current = current.next
                current.next = node    
        except Exception as error:
          raise Exception(f"Something Wrong : {error}")



    def includes(self,n):
        
        try:
          result=False

          current = self.head
          while current:
              if current.value==n:

                  result=True
                  break
              current=current.next
          return result
        except Exception as error:
          raise Exception(f"Something Wrong : {error}")

   


    def __str__(self):
        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += f"( {value} ) => None"
                break
            output = output + f"( {value} ) => "
            current=current.next
        return output

    def addBefore(self, value, newOne):
        newNode = Node(newOne)
        if not self.head :
            self.head = newNode
        else:
            current = self.head
            while current.value != value:
                current=current.next
        exactNode = Node(value)
        exactNode.next=current.next
        current.value=newNode.value
        current.next=exactNode

    def addAfter(self, value, newOne):
        print("tesssssssssst")
        newNode = Node(newOne)
         #i made a new node {value:99, next:none}
        if not self.head :
            self.head = newNode
            
        else:
            current= self.head
            while current.value != value:
                current= current.next
               
        newNode.next = current.next
        current.next=newNode            
       
    def Kth (self, k):
        current = self.head
        counter = 0
        while current.next:
            current = current.next
            counter += 1 


        if k > counter :
            print ("choose value within the length of the list")
            return
        
        if k < 0 :
            print (' minus values not allowed')
            return
        current = self.head
        for x in range(counter - k):
            current = current.next
        print(current.value)
        return current.value


#####test#####

def test_greater_than_len():
    lList = LinkedList()
    lList.insert(5)
    lList.insert(6)
    lList.insert(7)
    lList.Kth(7)
    actual = "choose value within the length of the list"
    excepted = "choose value within the length of the list"
    assert actual == excepted

def test_same_len():
    lList = LinkedList()
    lList.insert(5)
    lList.insert(6)
    lList.insert(7)
    lList.Kth(2)
    actual = 5
    excepted = 5 
    assert actual == excepted

def test_not_positive():
    lList = LinkedList()
    lList.insert(5)
    lList.insert(6)
    lList.insert(7)
    lList.Kth(-15)
    actual = ' minus values not allowed'
    excepted = ' minus values not allowed' 
    assert actual == excepted

def test_len1():
    lList = LinkedList()
    lList.insert(5)
    lList.Kth(0)
    actual = 5
    excepted = 5 
    assert actual == excepted

def test_happy_path():
    lList = LinkedList()
    lList.insert(5)
    lList.insert(6)
    lList.insert(7)
    lList.insert(3)
    lList.insert(10)
    lList.Kth(2)
    actual = 7
    excepted = 7 
    assert actual == excepted


