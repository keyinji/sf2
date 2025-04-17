from animal import Animal

class Cat(Animal):
    def __init__(self):
        super().__init__(4)
        self.type = 'cat'

    def sleep(self, hours):
        if hours == None:
            print(f'cats sleep in warm and comfortable place')
        else:
            print(f'cats sleep in warm and comfortable place for {hours} hours')

    def __repr__(self):
        return f'{self.type} has {self.legs} legs'



if __name__ == "__main__":
    cat = Cat()
    print(cat)


    print()
    cat.walk()

    print()
    cat.sleep(4)