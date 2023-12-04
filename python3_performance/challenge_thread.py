import threading
import time

def process_order(order_id):
    print(f'Processing order with id = {order_id}')
    # time.sleep(1)
    for _ in range(100_000_000):
        pass
    print(f'Finished processing order with id = {order_id}')


t1 = threading.Thread(target=process_order, args=(10,))
t2 = threading.Thread(target=process_order, args=(20,))
t1.start()
t2.start()
