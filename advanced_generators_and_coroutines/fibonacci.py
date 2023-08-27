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

