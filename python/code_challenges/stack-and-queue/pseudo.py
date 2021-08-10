from stackQueue import *

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



if __name__=='__main__':

    pQueue= PseudoQueue()
    pQueue.enqueue(1)
    pQueue.enqueue(2)
    pQueue.enqueue(3)
    print(pQueue.data.top.value)
    pQueue.dequeue()
    print(pQueue.data.top.value)



