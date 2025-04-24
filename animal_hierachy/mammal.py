from animal import Animal

class Mammal(Animal):

    def reproduce(self) -> str:
        return super().reproduce() + '\n' + 'Mammals give birth to live young, and raise them until they can live independently.'

    def __repr__(self) -> str:
        return super().__repr__() + '\n' + 'Class: Mammal'
        
    
