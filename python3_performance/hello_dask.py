from dask.distributed import Client
def clean_order(order_id):
    for _ in range(100_000_000):
        pass
    print(f'Finished cleaning order with id = {order_id}')

if __name__ == '__main__':
    client = Client()
    client.map(clean_order, [10, 20])
