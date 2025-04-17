class Animal:
    def __init__(self, legs=0):
        self.legs = legs 

    def walk(self):
        print(f"this animal walks with {self.legs} legs")

    def sleep(self):
        print("he sleeps")
    
    def __repr__(self):
        return f'ANIMAL dont knw number if LEGS:{self.legs}'
    
    
if __name__ == "__main__":
    animal = Animal(4)
    print(animal)

    print()

    animal.sleep()