# kernprof -lv dictionary.py
import random
def search_list(big_list, items):
    count = 0
    for item in items:
        for order in big_list:
            if item  == order[0]:
                count += 1
    return count

def search_dictionary(big_dictionary, items):
    count = 0
    for item in items:
        if item in big_dictionary:
                count += 1
    return count

@profile
def main():
    SIZE = 100_1000
    big_list = []
    big_dictionary = {}
    for i in range(SIZE):
        big_list.append([i, 2 * i, i * i])
        big_dictionary[i] = [i, 2 * i, i * i]

    orders_to_search  = [random.randint(0, SIZE) for _ in range(1000)]

    search_list(big_list, orders_to_search)
    search_dictionary(big_dictionary, orders_to_search)


main()
