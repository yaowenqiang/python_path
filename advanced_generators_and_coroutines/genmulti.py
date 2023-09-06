import threading, queue
from genqueue import genfrom_queue
from gencat import gen_cat

def multiplex(sources):
    in_q = queue.Queue()
    consumers = []
    for src in sources:
        thr = threading.Thread(target=sendto_queue, args=(src, in_q))
        thr.start()
        consumers.append(genfrom_queue(in_q))

    return gen_cat(consumers)
