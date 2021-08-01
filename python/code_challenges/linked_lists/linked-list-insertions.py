class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value='null'):
    
        try:
            print(self, '******************55555')
            node = Node(value)
            if not self.head:
                self.head = node
            else:
                current=self.head
                print('********',current)
            while current.next != None:
                current = current.next
                current.next = node    
        except Exception as error:
          raise Exception(f"Something Wrong : {error}")



if __name__ == "__main__":

    lList = LinkedList()
    lList.append(5)
    print(lList)