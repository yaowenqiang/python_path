from collections import deque

# kernprof -lv dequeue.py


@profile
def main():
    SIZE = 100_100
    big_list = list(range(SIZE))
    big_queue = deque(big_list)

    while big_list:
        big_list.pop()

    while big_queue:
        big_queue.pop()

    big_list = list(range(SIZE))
    big_queue = deque(big_list)

    while big_list:
        big_list.pop(0)

    while big_queue:
        big_queue.popleft()



main()

