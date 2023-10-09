import threading
x = 0
class Foo(object):
    lock = threading.RLock()

    def bar(self):
        global x
        with Foo.lock:
            x += 1

    def spam(self):
        global x
        with Foo.lock:
            x -= 1
            self.bar()



if __name__ == '__main__':
    f = Foo()
    f.spam()
