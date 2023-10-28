class OneShortNamespace(dict):
    def __init__(self, name, existing=None):
        super().__init__()
        self._name = name
        if existing is not None:
            for k, v in existing.items():
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError(f'can not reassign attribute {key!r} of class {self._name!r}')
        super().__setitem__(key, value)

class ProhibitDuplicateMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return OneShortNamespace(name)
    # return OrderedDict()

class Dodgy(metaclass=ProhibitDuplicateMeta):
    def method(self):
        return 'first definition'


    def method(self):
        return 'second definition'

if __name__ == '__main__':
    d = OneShortNamespace()
    d['a'] = 1
    d['b'] = 2
    # d['a'] = 3
    d = Dodgy()