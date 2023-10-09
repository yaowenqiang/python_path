import threading
import requests

sema = threading.Semaphore(5)

def fetch_page(url):
    sema.acquire()
    try:
        u = requests.get(url)
        return u.read()
    finally:
        sema.release()
