import threading
import time

init = threading.Event()

def worker():
    init.wait()
    time.sleep(10)

def initialize():
    time.sleep(10)
    init.set()

threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
initialize()
