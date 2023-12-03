import numpy as np
import random

def multiple_assignment(order):
    """
    Multiple assignments
    """
    order_subtotal, order_tax, order_shipping = order

def individual_assignment(order):
    """
    Multiple assignments
    """
    order_subtotal = order[0]
    order_tax = order[1]
    order_shipping = order[2]


@profile
def main():
    orders = [(random.randint(0, 100),
              random.randint(0, 100),
              random.randint(0, 100)) for _ in range(10000)]
    for o in orders:
        multiple_assignment(o)
        individual_assignment(o)

main()