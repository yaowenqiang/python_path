import time

@profile
def heavy_work():
    print('do something')
    print('do something')
    print('do something')
    for _ in range(100_100_100):
        pass
    print('do something')
    print('do something')

start_time = time.time()
heavy_work()
end_time = time.time()
print(f'duration: {end_time - start_time}')
