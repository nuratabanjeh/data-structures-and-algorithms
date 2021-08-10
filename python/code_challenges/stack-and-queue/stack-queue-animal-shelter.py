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


   





if __name__ == "__main__":
    buddy = Dog('buddy')
    milo=Dog('milo')
    lucky=Dog('lucky')
    bella = Cat('bella')
    lolo=Cat('lolo')
    kitty=Cat('kitty')
    
    frog=Animal('frog','rabbit')
    animalsh=AnimalShelter()
    animalsh.enqueue(buddy)
    animalsh.enqueue(milo)
    animalsh.enqueue(lucky)
    # animalsh.enqueue(bella)
    # animalsh.enqueue(lolo)
    # animalsh.enqueue(kitty)
    print(animalsh.enqueue(frog))
   
    # print(animalsh.dequeue('cat'))
    print(animalsh.dequeue('dog'))
    # print(animalsh)
