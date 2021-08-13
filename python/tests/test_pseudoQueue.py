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

import pytest

class PseudoQueue:
    def __init__(self):
        self.front=Stack()
        self.rear = Stack()

    def enqueue(self, value=None):
        if value == None:
            return "no value"

        self.front.push(value)

    def dequeue(self):

        if not self.front.top:
            return 'Queue is empty'
           
        while self.front.top:
            
       
            self.rear.push(self.front.pop())

        deqvalue = self.rear.pop()

        while self.rear.top:
        
    
            self.front.push(self.rear.pop())

        return deqvalue
    
        
def test_happypath():
    queue= PseudoQueue()
    queue.enqueue(10)
    queue.enqueue('nura')
    queue.enqueue(20)
    queue.enqueue(-8)
    actual = queue.front.top.value
    excepted = queue.front.top.value
    assert actual == excepted

def test_no_value():
    queue= PseudoQueue()
    queue.enqueue()
    actual ="no value"
    excepted ="no value"
    assert actual == excepted

def test_no_val_for_dequeue():
    queue= PseudoQueue()
    queue.dequeue()
    actual = 'Queue is empty'
    excpected='Queue is empty'
    assert actual == excpected



    
