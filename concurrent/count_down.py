import time
import threading
x = 10

class Countdownthread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            print(f'Counting down {self.count}')
            self.count -= 1
            time.sleep(1)
        return

def count_down(count):
    while count > 0:
            print(f'Counting down {count}')
            count -= 1
            time.sleep(1)

def reduce_one():
    global x
    while x > 0:
        x -= 1
        print(x)
        time.sleep(1)

def plus_one():
    global x
    while x < 20:
        x += 1
        print(x)
        time.sleep(1)

if __name__ == '__main__':
    t1 = Countdownthread(10)
    #count_down.run()
    t1.start()
    t1.join()
    t2 = Countdownthread(10)
    #count_down.run()
    t2.setDaemon(True)
    t2.start()
    t2.join()
    t3 = threading.Thread(target=count_down, args=(10,))
    t3.daemon = True
    t3.setDaemon(True)
    t3.start()
    t3.join()

    t4 = threading.Thread(target=reduce_one)
    t4.start()
    t4.join()
    t5 = threading.Thread(target=plus_one)
    t5.start()
    t5.join()
