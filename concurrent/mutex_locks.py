import threading

x = 0
x_lock = threading.Lock()

def reduce():
    global x
    x_lock.acquire()
    try:
        x = x - 1
    finally:
        x_lock.release()

def plus():
    global x
    x_lock.acquire()
    try:
        x = x + 1
    finally:
        x_lock.release()

def divide():
    global x
    with x_lock:
        x = x / 2


if __name__ == '__main__':
    t1 = threading.Thread(target=plus)
    t2 = threading.Thread(target=reduce)
    t3 = threading.Thread(target=divide)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    print(x)


