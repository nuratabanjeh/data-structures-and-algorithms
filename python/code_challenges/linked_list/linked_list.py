class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):
        """
        Adds a node of a value to the head of LL
        """
        try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")


    def append(self, value='null'):
        """
        Adds a node of a value to the end of LL
        """
        try:
          node = Node(value)
          if not self.head:
              self.head = node

          else:
              current = self.head
              while current.next != None:
                  current = current.next
              current.next = node
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")

    def includes(self,num):
        """
        Return T/F if value is in the linked list or not
        """
        try:
          x=False

          current = self.head
          while current:
              if current.value==num:

                  x=True
                  break
              current=current.next
          return x
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")

    def insertBefore(self ,value, newVal):
        """
        add a new node with the given newValue immediately before the first value node
        """
        current = self.head
        if current.value==value:
            self.insert(newVal)
        else:
          while current:

             if current.next.value==value :
                nextvalue=current.next
                current.next=Node(newVal)
                current.next.next=nextvalue
                break
             current=current.next


    def insertAfter(self, value, newVal):
        """
        add a new node with the given newValue immediately after the first value node
        """
        current = self.head
        while current:
            if current.value==value :
                nextvalue=current.next
                current.next=Node(newVal)
                current.next.next=nextvalue
                break
            current=current.next

    def kthFromEnd(self,k):
        if type(k)!=type(5):
            return 'Please enter number input'
        if k<0:
            return "Can't enter negative input"
        valuelist=[]
        current = self.head
        while current:
            valuelist+=[current.value]

            current=current.next
        if k==0:
            return valuelist[-1]
        else:
            if k>=len(valuelist):
                return 'Exception'
            return valuelist[(k*-1)-1]





    def __str__(self):
        """
        Loop over all nodes
        print all values in one line
        ( a ) -> ( b ) -> ( c ) -> None
        """

        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += f"( {value} ) -> None"
                break
            output = output + f"( {value} ) -> "
            current=current.next
        return output


def palindrome(ll):
  valuelist=[]
  current = ll.head
  while current:
    valuelist+=[current.value]
    current=current.next

  for i in range(len(valuelist)//2):
    if valuelist[i]!=valuelist[-1*i-1]:
      return False
  return True

def reverse(ll):
  valuelist=[]
  x='head->'
  current = ll.head
  while current:
    valuelist+=[current.value]
    current=current.next
  print(valuelist)
  for i in range(len(valuelist)):
      if i==len(valuelist)-1:
          x+=f'({valuelist[-1*i-1]})'
      else:
          x+=f'({valuelist[-1*i-1]})->'

  return x











if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(1)

    # ll.append(1)
    # ll.append(4)
    print(ll.__str__())
    print(palindrome(ll))
    # print(reverse(ll))
