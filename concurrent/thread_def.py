import time
import threading

class CountdownThread(threading.Thread):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        while self.count > 0:
            print("Counting down", self.count)
            self.count -= 1
            time.sleep(5)
        return

t1 = CountdownThread(10)
t1.start()
t1.join()

t2 = CountdownThread(20)
t2.start()
t2.join()
