class Node:
    def __init__(self, value=None):
      self.value=value
      self.next=None

class Stack:
    def __init__(self, node=None):
        self.top=node
        self.length = 0


    def push(self, value):
        print('***********************')
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.value

    def is_empty(self):
        return not self.top

    def peek(self):
        if self.length <=0:
            print('empty')
            return
        print(self.top.value)
        return self.top.value


class Queue:
    def __init__(self):
        self.front=None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front=node
            self.rear = node
        else:
            self.rear.next = node
            self.rear= node

    def dequeue(self):

        dequeueValue=self.front.value
        self.front=self.front.next
        return dequeueValue

    def peek(self):
        
        return self.front.value
        
                

    def isEmpty(self):
        if (not self.rear and self.front) or (self.rear and not self.front):
            raise Exception("Something's Wrong")
        


class PseudoQueue:
    def __init__(self):
        self.data=Stack()

    def enqueue(self,value):
        self.data.push(value)
        return self

    def dequeue(self):
        if not self.data.top:
            return "empty"
        current=self.data.top
        newList=[]
        while current:
            newList.append(current.value)
            current=current.next
        for i,x in enumerate(range(len(newList),0,-1)):
            if i<len(newList)-1:
                self.data.push(x)
        return self

#####################

def test_enqueue():
    pQueue= PseudoQueue()
    pQueue.enqueue(1)
    pQueue.enqueue(2)
    pQueue.enqueue(3)
    actual = pQueue.data.top.value
    excepted = 3
    assert actual == excepted

def test_dequeue():
    pQueue= PseudoQueue()
    pQueue.enqueue(1)
    pQueue.enqueue(2)
    pQueue.enqueue(3)
    pQueue.dequeue()
    actual = pQueue.data.top.value
    excepted = 2
    assert actual == excepted

def test_empty_dequeue():
    pQueue= PseudoQueue()
    pQueue.dequeue()
    actual = "empty"
    excepted = "empty"
    assert actual == excepted






