import time
import threading

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
