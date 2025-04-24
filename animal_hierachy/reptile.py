from animal import Animal

class Reptile(Animal):

    def reproduce(self) -> str:
        return super().reproduce() + '\n' + 'Reptiles reproduce by laying eggs, typically on land rather than water.'
    
    def __repr__(self) -> str:
        return super().__repr__() + '\n' + 'Class: Reptile' 