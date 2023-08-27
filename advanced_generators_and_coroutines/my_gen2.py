def generator():
    print("Entering")
    yield 1
    print('Wait me please')
    yield 2
    print('I am thinking the next one')
    yield 3
    print('Exiting')


for i in generator():
    print(f'-> {i}')

