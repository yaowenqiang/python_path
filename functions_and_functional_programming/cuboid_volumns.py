def _hypervolume(*args):
    print(args)
    print(type(args))
def __hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= length
    return v
