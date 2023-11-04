from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

[x for x in range(101) if is_prime(x)]
prime_square_divisor = {x*x: (1,x,x*x) for x in range(20) if is_prime(x)}
