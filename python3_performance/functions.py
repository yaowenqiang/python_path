import random

def get_random_integer():
    return random.randint(0, 100)

@profile
def main():
    [random.randint(0, 100) for _ in range(10000)]
    [get_random_integer() for _ in range(10000)]
    [(lambda: random.randint(0, 100))() for _ in range(10000)]
main()