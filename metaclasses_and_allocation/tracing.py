from icecream import ic
class TracingMeta(type):
    @classmethod
    def __prepare__(scs, name, bases, **kwargs):
        print('TracingMeta.__prepare__(name, bases, **kwargs)')
        ic(scs)
        ic(name)
        ic(bases)
        ic(kwargs)
        namespace = super().__prepare__(name, bases)
        ic(namespace)
        return namespace

    def __new__(scs, name, bases, namespace, **kwargs):
        print('TracingMeta.__new__(name, bases, namespace,**kwargs)')
        ic(scs)
        ic(name)
        ic(bases)
        ic(namespace)
        ic(kwargs)
        cls = super().__new__(scs, name, bases, namespace)
        ic(cls)
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print('TracingMeta.__init__(name, bases, namespace,**kwargs)')
        ic(cls)
        ic(name)
        ic(bases)
        ic(namespace)
        ic(kwargs)
        super().__init__(name, bases, namespace)
        ic(cls)


    def __call__(cls, *args, **kwargs):
        print('TracingMeta.__call__(cls, *args, **kwargs)')
        ic(cls)
        ic(args)
        ic(kwargs)
        ic('About to  call type.__call__')
        obj = super().__call__(*args, **kwargs)
        ic('Returned from type.__call__')
        ic(obj)
        ic()
        return obj

    def metamethod(cls):
        ic('TracingMeta.metamethod(cls)')
        ic(cls)
        

class Widget(metaclass=TracingMeta):
    the_answer = 42
    def action(self, message):
        ic(message)

class TracingClass(metaclass=TracingMeta):
    def __new__(cls, *args, **kwargs):
        print('TracingClass.__new__(cls, *args, **kwargs)')
        ic(cls)
        ic(args)
        ic(kwargs)
        obj = super().__new__(cls)
        ic()
        ic(obj)
        return obj

    def __init__(self, *args, **kwargs):
        print('TracingClass.__init__(self, *args, **kwargs)')
        ic(self)
        ic(args)
        ic(kwargs)
        super().__init__(*args, **kwargs)
        ic()


if __name__ == '__main__':
    t = TracingClass()