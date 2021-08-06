class Node:
    def __init__(self, value=None):
      self.value=value
      self.next=None

class Stack:
    def __init__(self, node=None):
        self.top=node
        self.length = 0


def push(self, value):
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
       

if __name__=='__main__':
    stack=Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.pop()

    queue=Queue()
    queue.enqueue()
    queue.peek()
