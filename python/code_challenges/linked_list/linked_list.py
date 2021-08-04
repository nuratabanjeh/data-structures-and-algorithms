class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
    print(lList.includes(300))
    print(lList)
  
 
