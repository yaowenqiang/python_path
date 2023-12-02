import random


@profile
def main():
    orders = [random.randint(0, 100) for _ in range(10000)]
    comprehension = [2 * x for x in orders if x > 50]
    generator = (2 * x for x in orders if x > 50)

    sum(comprehension)
    sum(generator)

main()