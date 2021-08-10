class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, node=None):
        self.top= node
        


    def push(self, value):
        node= Node(value)
        node.next = self.top
        self.top = node


    def pop (self):
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except:
            return("empty")

    def peek(self):
        try:
           return self.top.value
        except:
            return("empty")

    def isEmpty(self):
        return not self.top

class Queue:
    def __init__(self):
        self.front = None
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
        try:
            remove=self.front.value
            self.front=self.front.next
            return remove
        except: 
            return "empty"

    def peek(self):
        try:
            return self.front.value
        except:
            return("empty")

    def isEmpty(self):
        if (not self.rear and self.front) or (self.rear and not self.front):
          raise Exception("empty")
        return not self.rear


if __name__ == "__main__":
    stacke=Stack()
    print(stacke,'hyoooooooooooo')
    stacke.push('hello')
    

    # stacke.pop()

    # stacke.pop()
    print(stacke.top.value)

    stacke.push(5)
    stacke.push(8)
    print(stacke.top.value)
    print(stacke.peek(), 'woooooow')
    print(stacke)
    print(stacke.isEmpty())

    queue=Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.enqueue(5), "hiiiiii")

    print(queue.dequeue())

    


