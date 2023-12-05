import threading

import requests


def download():
    return requests.get('https://www.python.org').content

def single_thread():
    for _ in range(5):
        download()


def multiple_thread():
    threads = [threading.Thread(target=download) for _ in range(5)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

@profile
def main():
    single_thread()
    multiple_thread()

main()