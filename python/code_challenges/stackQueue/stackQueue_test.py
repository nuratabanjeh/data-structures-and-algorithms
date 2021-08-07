from stackQueue import *
# import pytest

def test_push():
    stack=Stack()
    stack.push(7)
    stack.push(8)
    stack.push(9)
    actual = stack.top.value
    expected= 9
    assert actual == expected

def test_pop():
    stack=Stack()
    stack.push(7)
    stack.push(8)
    stack.pop()
    actual = 8
    expected= 8
    assert actual == expected 

def test_multi_pop():
    stack=Stack()
    stack.push(7)
    stack.push(8)
    stack.pop()
    stack.pop()
    actual = "empty stack"
    expected= "empty stack"
    assert actual == expected 

def test_peek():
    stack=Stack()
    stack.push(7)
    stack.push(8)
    stack.peek()
    actual = 8
    excepted = 8
    assert actual == excepted
    
def test_emptyStack():
    stack=Stack()
    stack.pop()
    stack.peek()
    assert stack.pop() == "empty"
    assert stack.peek() == "empty"


def test_enqueue():
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    actual = 10
    expected= 10
    assert actual == expected 

def test_dequeue():
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.dequeue()

    actual = 10
    expected= 10
    assert actual == expected 

def test_peek():
    queue=Queue()
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.peek() == 20

def test_empty_queue():
    queue=Queue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.dequeue() == "empty"
    assert queue.peek() == "empty"
    





