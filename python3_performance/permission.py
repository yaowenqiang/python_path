import random


def permission(orders):
    result = []
    for amount in orders:
        if type(amount) == int:
            if amount > 50:
                result.append(2 * amount)
    return result

def forgivess(orders):
    result = []
    for amount in orders:
        try:
            if amount > 50:
                result.append(2 * amount)
        except TypeError:
            pass
    return result


@profile
def main():
    orders = [random.randint(0, 100) for _ in range(10000)]
    for i in range(10):
        orders[i] = 'bad data'
    permission(orders)
    forgivess(orders)

    for i in range(9000):
        orders[i] = 'bad data'
    permission(orders)
    forgivess(orders)

main()