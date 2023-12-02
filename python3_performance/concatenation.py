import random


@profile
def main():
    orders = [str(random.randint(0, 100)) for _ in range(50000)]
    report = ''
    for i in orders:
        report += i

    ''.join(orders)

main()