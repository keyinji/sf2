from pet import Pet
from herbivore import Herbivore
from mammal import Mammal

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        Mammal.__init__(self, legs)
        self.ears = ears

    def __repr__(self) -> str:
        return 'Species: Bunny' +'\n' + Mammal.__repr__(self) + '\n' + Herbivore.__repr__(self) + '\n' + Pet.__repr__(self)
    
    def reproduce(self) -> str:
        return Mammal.reproduce(self) + '\n' + 'Bunnies are born.'

    def eat(self) -> None:
        Herbivore.eat(self)
        print("Bunnies eat plants.")
    
    def sleep(self) -> None:
        print("Bunnies sleep.")

    def move(self) -> None:
        print("Bunnies hop.")

if __name__ == "__main__":
    bunny = Bunny()
    print(bunny)
    print()
    bunny.reproduce()
    print()
    bunny.eat()
    print()
    bunny.sleep()
    print()
    bunny.move()
    print()
    print(bunny.pet())
    
