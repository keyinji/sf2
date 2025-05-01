from progression import Progressions
class GP(Progressions):
    def __init__(self, base = 2, start = 1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

        
    