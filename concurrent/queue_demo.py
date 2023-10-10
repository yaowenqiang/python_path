from queue import Queue
from icecream import ic

q = Queue(10)
q.put(1)
ic(q.empty())
ic(q.get())
ic(q.empty())
ic(q.full())
q.task_done()
q.join()
