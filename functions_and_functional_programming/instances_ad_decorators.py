class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap

trace = Trace()

@trace
def rotate_list(l):
    return l[1:] + [l[0]]

l = [1,2,3,4]
l = rotate_list(l)

trace = False
l = rotate_list(l)
l = rotate_list(l)
l = rotate_list(l)
l = rotate_list(l)




