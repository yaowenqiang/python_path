class Widget:
    pass

class Widget1(object, metaclass=type): # object is the default Base Class
    pass

class Widget1():
    name = 'Widget'
    bases = ()
    kwargs = {}
    namespace = metaClass.__prepare__(name, bases, **kwargs)
    Widget = metaclass.__new__(metaclass, name, bases, namespace, **kwargs)
    metaclass.__init__(Widget, name, bases, namespace, **kwargs)




if __name__ == '__main__':
    w = Widget()
    print(type(w))
    print(type(Widget))
    print(w.__class__)
    print(w.__class__.__class__)
    print(w.__class__.__class__.__class__)
