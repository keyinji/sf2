from progression import Progressions

class AP(Progressions):
    def __init__(self, increment = 1, start = 0):
        '''create new arithmetic progression'''
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        '''update current values'''
        self._current += self._increment 

if __name__ == "__main__":
    AP(5, 10).printProgression(10)

    for value in AP(5).lst(5):
        print(value*2)