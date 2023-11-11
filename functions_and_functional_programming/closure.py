def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func

lf = enclosing()
lf()
print(lf.__closure__)
