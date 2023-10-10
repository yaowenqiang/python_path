import threading

cv = threading.Condition([lock])
cv.acquire()
cv.release()
cv.wait()
cv.notify()
cv.notifyall()
