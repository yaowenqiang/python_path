import inspect
def my_coroutine(a):
    print(f' --> Started with {a}')
    b = yield
    print(f'But continues with {b}')


mycoro  = my_coroutine(2)
print(inspect.getgeneratorstate(mycoro))
next(mycoro)
print(inspect.getgeneratorstate(mycoro))
mycoro.send(5)
print(inspect.getgeneratorstate(mycoro))
