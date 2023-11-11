import time
message = 'global'
def enclosing():
    message = 'enclosing'
    def local():
        #global message
        nonlocal message
        message = 'local'
    print('enclosing messages', message)
    local()
    print('enclosing messages', message)

print('global messages', message)
enclosing()
print('global messages', message)


def make_timer():
    last_called = None # Never
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed


t = make_timer()
t()
t()
t()
t()
t()
t()
