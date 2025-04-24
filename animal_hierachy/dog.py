from pet import Pet
from carnivore import Carnivore
from mammal import Mammal

class Dog(Mammal, Carnivore, Pet):
    def __init__(self, legs=4, tail=1):
        Mammal.__init__(self, legs)
        self.tail = tail

    def __repr__(self) -> str:
        return 'Species: Dog' +'\n' + Mammal.__repr__(self) + '\n' + Carnivore.__repr__(self) + '\n' + Pet.__repr__(self)

    def move(self) -> None:
        print("Dogs run and walk.")

    def sleep(self) -> None:
        print("Dogs sleep.")

    def eat(self) -> None:
        Carnivore.eat(self)
        print("Dogs eat dog food and meat.")

    def reproduce(self) -> str:
        return Mammal.reproduce(self) + '\n' + 'Puppies are born.'
    
    def pet(self) -> str:
        return Pet.pet(self)

if __name__ == "__main__":
    dog = Dog()
    print(dog)
    print()
    print(dog.reproduce())
    print()
    dog.eat()
    print()
    dog.sleep()
    print()
    dog.move()
    print()
    print(dog.pet()) 