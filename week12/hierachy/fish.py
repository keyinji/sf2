from animal import Animal
from __future__ import annotations

class Fish(Animal):
    def __init__(self, color):
        # super().__init__(0)
        self.type = 'fish'
        self.color = color
    
    def sleep(self):
        print(f'fish sleep with eyes open in water')    
    def walk(self):
        print(f'fish dont walk')
    
    def __repr__(self):
        return f'{self.type} has {self.color} color'
    
    def changeColor(self, color):
        self.color = color

    def sameColor(self, other: Fish) -> bool:
        return self.color == other.color

if __name__ == "__main__":
    fish = Fish('red')
    print(fish)

    print()
    fish.sleep()
    fish.walk()

    print()
    fish.changeColor('blue')
    print(fish)

    print()
    fish2 = Fish('blue')
    print(fish2)
    
