from linked_list import *
# import pytest
def test_empty_linkedList():
    lList = LinkedList()
    actual = lList.head
    assert actual == None

def test_insert():
    lList = LinkedList()
    lList.insert(6)
    lList.insert(8)
    actual= lList.head.value
    actualNone = lList.head.next.value
    excepted = 6
    print(actual)
    
    assert lList.head.value == 8
    assert actualNone == 6

def test_includes():
    lList=LinkedList()
    lList.insert(7)
    lList.insert(15)
    lList.insert(70)
    actual=lList.includes(70)
    excepted=True

    assert actual == excepted
    
def test_False_includes():
    lList=LinkedList()
    lList.insert(7)
    lList.insert(15)
    actual=lList.includes(70)
    excepted=False

    assert actual == excepted

def test_everyThing_print():
    lList=LinkedList()
    lList.insert(10)   
    lList.insert(20)    
    lList.insert(30)   
    lList.__str__()
    actual = '( 30) =>( 20) =>( 10) => None'
    excepted = '( 30) =>( 20) =>( 10) => None'

    assert actual == excepted


    # ###########code ch 2################

def test_adding_node():
    lList=LinkedList()
    lList.insert(1)
    lList.insert('bla blaaaa')
    lList.append(5)
    lList.__str__()
    actual = '( bla blaaaa ) -> ( 1 ) -> ( 5 ) -> None'
    expected='( bla blaaaa ) -> ( 1 ) -> ( 5 ) -> None'
    assert actual==expected

def test_add_before():
    lList = LinkedList()
    lList.append(10)
    lList.append(30)
    lList.append(40)
    lList.addBefore(30, 20)
    lList.__str__()

    actual = '( 10 ) -> ( 20 ) -> ( 30 ) -> ( 40 ) -> None'
    expected='( 10 ) -> ( 20 ) -> ( 30 ) -> ( 40 ) -> None'
    assert actual==expected

def test_add_after():
    lList = LinkedList()
    lList.append(10)
    lList.append(30)
    lList.append(40)
    lList.addAfter(30, 20)
    lList.__str__()

    actual = '( 10 ) -> ( 30 ) -> ( 20 ) -> ( 40 ) -> None'
    expected='( 10 ) -> ( 30 ) -> ( 20 ) -> ( 40 ) -> None'
    assert actual==expected

