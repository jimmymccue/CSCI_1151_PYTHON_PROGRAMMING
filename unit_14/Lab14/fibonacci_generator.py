class FibonacciGenerator:
    """
    Generator class for Fibonacci numbers.
    """

    def __init__(self):
        """
        Initialize the first two Fibonacci numbers.
        """
        self.a = 0
        self.b = 1
    
    def next(self):
        """
        Return the next Fibonacci number in the sequence.
        """
        fib_num = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib_num
