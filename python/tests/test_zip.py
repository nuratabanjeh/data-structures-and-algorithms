# from code_challenges.linked_lists.zip import *
# from code_challenges.linked_lists.linked_list import (Node,LinkedList)
from python.code_challenges.linked_lists.zip import zipList


class Node:
    def __init__(self, value= None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value='null'):
    
       
            print(self)
            node = Node(value)
            if not self.head:
                self.head = node
            else:
                print(self)

                current=self.head
                while current.next != None:
                  current = current.next
                current.next = node    
        
        

    def zipList(list1,list2):
            current1=list1.head
            current2=list2.head
            if current1 == None and current2 == None:
             return("empty")

            if not current1:
                list1.head = list2.head
                return list1.head

            if not current2:
                return list1.head

            temp = current2.next

            while current1.next and current2.next:
                current1.next, current2.next = current2, current1.next
                current1 = current2.next
                current2, temp = temp, temp.next

            if not current1.next:
                current1.next = current2
                return list1.head

            if not current2.next:
                current1.next, current2.next = current2, current1.next
                return list1.head



def test_zip_fun():
    lList=LinkedList
    lList.append(1)
    lList.append(2)
    lList.append(3)
    lList1=LinkedList
    lList1.append(10)
    lList1.append(20)
    lList1.append(30)
    actual= zipList(lList, lList1)
    excepted = "( 1 ) => ( 10 ) => ( 2 ) => ( 20 ) => ( 3 ) => ( 30 ) => None"
    assert actual == excepted