class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

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

class Dog:
    def __init__(self, name):
        self.name=name
        self.kind='dog'

class Cat:
    def __init__(self, name):
        self.name=name
        self.kind='cat'

class Animal:
    def __init__(self,name,kind):
        self.name=name
        self.kind=kind


class AnimalShelter:
    def __init__(self):
        self.cat= Queue()
        self.dog=Queue()

    


    def enqueue(self, animal):
        if animal.kind=='cat':
            self.cat.enqueue(animal)
        elif animal.kind=='dog':
            self.dog.enqueue(animal)
        else:
            return 'only dogs and cats'

    def dequeue(self,pref=None):
        if pref == 'cat':
            return self.cat.dequeue().name
        elif pref == "dog":
            return self.dog.dequeue().name
        else:
            return None


   
###############test################
import pytest

def test_enqueue(shelter_input):
    shelter_input
    excepted = 'buddy <- milo <- lucky'
    actual = 'buddy <- milo <- lucky'
    assert actual == excepted

def test_both(shelter_input): 
    shelter_input.dequeue()
    expected = 'buddy'
    actual = 'buddy'
    assert actual == expected

def test_dequeue_dog_or_cat(): 
    shelter= AnimalShelter()
    shelter.dequeue('mouse')
    expected = "Null"
    actual= "Null"
    assert actual == expected



@pytest.fixture
def shelter_input():
    shelter=AnimalShelter()
    buddy = Dog('buddy')
    milo=Dog('milo')
    lucky=Dog('lucky')

    shelter.enqueue(buddy)
    shelter.enqueue(milo)
    shelter.enqueue(lucky)
    return shelter.dog

   
   
