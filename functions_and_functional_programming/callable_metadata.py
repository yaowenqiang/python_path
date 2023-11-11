import functools
def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    #noop_wrapper.__name__ = f.__name__
    #noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper

@noop
def hello():
    "Print a well-known message."
    print('Hello world')

print(hello.__name__)
print(hello.__doc__)

