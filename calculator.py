"""
Calculator library containing basic math operations
"""

class Calculator():
    def __init__(self):
        self.cache = [0, 1]  # Initialize the cache in the constructor

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def fib(self, n):
        if not isinstance(n, int) or n < 0:
            raise TypeError('Invalid input for Fibonacci sequence')
        if n < len(self.cache):
            return self.cache[n]
        else:
            while len(self.cache) <= n:
                fib_number = self.cache[-1] + self.cache[-2]
                self.cache.append(fib_number)
            return self.cache[n]

    def __call__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise TypeError('Invalid input')

calc = Calculator()

while True:
    print('1 Add')
    print('2 Subtract')
    print('3 Multiply')
    print('4 Divide')
    print('5 Fib')
    print('6 Exit')

    choice = float(input('Choose a function: '))
    if choice in range(1, 7):
        if choice == 6:
            break

        if choice in [1, 2, 3, 4]:
            a = float(input('First number: '))
            b = float(input('Second number: '))

        if choice == 1:
            print(a, '+', b, '=', calc.add(a, b))
        elif choice == 2:
            print(a, '-', b, '=', calc.subtract(a, b))
        elif choice == 3:
            print(a, '*', b, '=', calc.multiply(a, b))
        elif choice == 4:
            print(a, '/', b, '=', calc.divide(a, b))
        elif choice == 5:
            n = int(input('Enter a non-negative integer for Fibonacci: '))
            print(f'The fib of {n} =', calc.fib(n))
        else:
            print('ERROR')
    else:
        print('Invalid choice, please select a valid option (1-6)')
