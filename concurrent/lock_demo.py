import threading
x = 0
def foo():
    global x
    for i in range(100000000):
        x += 1
def bar():
    global x
    for i in range(100000000):
        x -= 1

t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)
t1.start()
t1.join()
t2.start()
t2.join()
print(x)
