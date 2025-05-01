from progression import Progressions



class FibonacciProgression(Progressions):
    def __init__(self, first=0, second=1):
        """Initialize Fibonacci progression with first and second values."""
        super().__init__(first)
        self._prev = second - first  # Store value before first
        self._second = second       # Store second value

    def _advance(self):
        """Advance to the next Fibonacci number."""
        self._prev, self._current = self._current, self._prev + self._current

if __name__ == "__main__":
    # Test default Fibonacci progression (0, 1, 1, 2, 3, 5, ...)
    fib1 = FibonacciProgression()
    fib1.printProgression(8)  # Prints: 0 1 1 2 3 5 8 13

    # Test Fibonacci progression starting with 2, 4 (2, 4, 6, 10, 16, ...)
    fib2 = FibonacciProgression(2, 4)
    fib2.printProgression(6)  # Prints: 2 4 6 10 16 26

    # Test list method
    fib3 = FibonacciProgression()
    print(fib3.lst(5))  # Prints: [0, 1, 1, 2, 3]