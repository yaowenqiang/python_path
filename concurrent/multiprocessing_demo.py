import time
import multiprocessing
class CountdownProcess(multiprocessing.Process):
    def __init__(self, count):
        multiprocessing.Process.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            print("Counting down", self.count)
            self.count -= 1
            time.sleep(0)
        return

if __name__ == '__main__':
    p1 = CountdownProcess(10)
    p1.start()
    p2 = CountdownProcess(10)
    p2.start()
