
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
        newNode= Node(k)
        indexList=[]
        if not self.head:
            print('Exception')   

        current =self.head
        while current.next:
            indexList.append(current.value)
            current=current.next
        indexList.append(current.value)
        indexList.reverse()  
        print(indexList)
        i=0  
        for value in indexList:
            if i == k:
                print(value)
                break
            i+=1 
        if k > len(indexList) :
                print('Exception') 
                return          
        if k == len(indexList):
            print('Exception')    
            return
        if k < 0:
            print('Exception')    
            return
    





if __name__ == "__main__":

    lList = LinkedList()
    print(lList)
    lList.insert(5)
    print(lList)
    lList.insert(6)
    print(lList)
    print(lList.includes(6))
    print(lList)
    lList.includes(4)
    print(lList.includes(4))
    print(lList)
    lList.append(10)
    print(lList)
    lList.addBefore(5,15)
    print(lList)
    lList.addAfter(15,99)
    print(lList)
    lList.Kth(3)
    print(lList)
    lList.Kth(7)
    print(lList)
    lList.Kth(5)
    print(lList)
    lList.Kth(-5)
    print(lList)