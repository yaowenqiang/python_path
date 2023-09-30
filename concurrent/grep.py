from icecream import ic
def grep(pattern):
    ic(f'looking for {pattern}')
    while True:
        line = (yield)
        if pattern in line:
            ic(line)



msg  = 'hello world\n how are you doing today?'
g = grep('hello')
g.send(None)
g.send(msg)
