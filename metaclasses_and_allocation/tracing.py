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

class Widget(metaclass=TracingMeta):
    the_answer = 42
    def action(self, message):
        ic(message)
