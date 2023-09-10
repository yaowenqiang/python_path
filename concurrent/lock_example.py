import threading
import time
class Foo(object):
    lock = threading.RLock()
    def bar(self):
        with Foo.lock:
            self.spam()

    def spam(self):
        with Foo.lock:
            self.bar()

f = Foo()
f.spam()

