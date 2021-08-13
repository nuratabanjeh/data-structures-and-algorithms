from linked_list import (Node , LinkedList )



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



if __name__ == "__main__":

    lList = LinkedList()
    # print(lList)
    lList.insert(5)
    # print(lList)
    lList.insert(6)
   
   
    lList.append(10)
  
    lList1=LinkedList()
    lList1.insert(50)
    lList1.append(60)
    lList1.append(70)
    print(lList1)
    
    zip=zipList(lList, lList1)
    print(zipList(lList, lList1))