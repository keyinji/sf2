class Progressions:
    def __init__(self, start=0, max_terms=None):
        """Initialize progression with starting value and optional max terms."""
        self._current = start
        self._max_terms = max_terms
        self._term_count = 0

    def _advance(self):
        """Advance to the next term in the progression.

        Should be overridden by subclasses to customize the progression.
        """
        self._current += 1

    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """Return the next element or raise StopIteration."""
        if self._max_terms is not None and self._term_count >= self._max_terms:
            raise StopIteration
        answer = self._current
        self._advance()
        self._term_count += 1
        return answer

    def printProgression(self, n):
        """Print the next n values of the progression."""
        print(' '.join(str(self.__next__()) for _ in range(n)))

    def lst(self, n):
        """Return a list of the next n values of the progression."""
        return [int(self.__next__()) for _ in range(n)]

if __name__ == "__main__":
    # Test default progression starting at 0
    prog1 = Progressions()
    prog1.printProgression(6)  # Prints: 0 1 2 3 4 5

    # Test progression starting at 12
    prog2 = Progressions(12)
    prog2.printProgression(6)  # Prints: 12 13 14 15 16 17