from icecream import ic
class EntriesMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        ic('EntriesMeta.__new__(mcs, name, bases, namespace, **kwargs)')
        ic(kwargs)
        num_entries = kwargs['num_entries']
        ic(num_entries)
        namespace.update({chr(i): i for i in range(ord('a'), ord('a') + num_entries)})
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


class AtoZ(metaclass=EntriesMeta, num_entries=26):
    pass
