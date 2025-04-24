from animal import Animal

class Amphibian(Animal):
    
    def reproduce(self) -> str:
        return super().reproduce() + '\n' + 'Amphibians reproduce by laying soft eggs in the water.'
    
    def __repr__(self) -> str:
        return super().__repr__() + '\n' + 'Class: Amphibian' 