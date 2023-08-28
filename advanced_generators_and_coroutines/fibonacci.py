import timeit
import numpy as np

def fibonacci(n):
    if n < 0:
        print('incorrect input')
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return  fibonacci(n-1) + fibonacci(n - 2)


def fibonacci_optmized(n):
    a = 1
    b = 2
    if n < 0:
        print('incorrect input')
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

class FibonacciIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'FibonacciIterable({self.start, self.end})'

    def __iter__(self):
        return FibonacciIterator(self.start, self.end)

class FibonacciIterator:
    def __init_-(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0

    def __next__(self):
        if self.start  + self.increment > self.end:
            raixe StopIteration()

        fibonacci_number = fibonacci(self.start + self.increment)
        self.increment += 1
        return fibonacci_number

    def __iter__(self):
        return self


class FibonacciGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __repr__(self):
        return f'FibonacciGenerator({self.star, self.endt})''

    def __iter__(self):
        for i in range(self.start, self.end):
            yield fibnacci(i)


class FibonacciGeneratorOptmized:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'FibonacciGeneratorOptmized({self.star, self.endt})''

    def __iter__(self):
        for i in range(self.start, self.end):
            yield fibnacci_optmized(i)


class FibonacciGeneratorLazyOptmized:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.fibonacci_dict = {i: fibnacci_optmized(i) for i in range(self.start, self.end+1)}
        self.increment = 0

    def __repr__(self):
        return f'FibonacciGeneratorLazyOptmized({self.star, self.endt})''

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield self.fibonacci_dict[i]


class FibonacciIterableLazyOptmized:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0

    def __repr__(self):
        return f'FibonacciIterableLazyOptmized({self.star, self.endt})''


    def __iter__(self):
        return FibonacciIteratorLazyOptmized(self.start, self.end)


class FibonacciIteratorLazyOptmized:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.increment = 0
        self.fibonacci_dict  = {i: fibonacci_optmized(i) for i in range(self.start, self.end + 1)}

    def __next__(self):
        if self.start + self.increment > self.end:
            raise StopIteration()

        fibonacci_number = self.fibonacci_dict[self.start + self.increment]
        self.increment += 1
        return fibonacci_number


class Call:
    def __init__(self, it, start, end):
        self.it = it
        self.start = start
        self.end = end

    def __call__(self, *args, **kwargs):
        for _ in it(start=self.start, end=self.end):
            pass

if __name__ == '__main__':
    start_fib = 2
    end_fib = 20

    fibonacci_iterable = FibonacciIterable
    fibonacci_generator = FibonacciGenerator
    fibonacci_generator_lazy = FibonacciGeneratorOptmized
    fibonacci_generator_lazy_fast = FibonacciGeneratorLazyOptmized
    fibonacci_iterable_lazy_fast = FibonacciIterableLazyOptmized

    for iterable in [fibonacci_iterable, fibonacci_generator, fibonacci_generator_lazy, fibonacci_generator_lazy_fast, fibonacci_iterable_lazy_fast]:
        print(f'For the iterable {iterable} we got \n')
        print(f'{np.mean(timeit.repeat(Call(iterable, start_fib, end_fib), number=5, repeat=5))}\n')








































































