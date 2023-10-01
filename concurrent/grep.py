from icecream import ic
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        #ic(dir(cr))
        next(cr)
        return cr
    return start

@coroutine
def grep(pattern):
    ic(f'looking for {pattern}')
    while True:
        line = (yield)
        if pattern in line:
            ic(line)

msg  = 'hello world\n how are you doing today?'
g = grep('hello')
#g.send(None)
g.send(msg)



