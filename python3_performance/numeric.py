import numpy as np
import random

def loop_approach(orders):
    sum = 0
    for i in orders:
        sum += i * i
    return sum

def numpy_approach(orders):
    numpy_orders = np.array(orders)
    return np.sum(numpy_orders * numpy_orders)

@profile
def main():
    orders = [random.randint(0, 100) for _ in range(10000)]
    loop_approach(orders)
    numpy_approach(orders)
main()