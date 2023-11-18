from icecream import ic
class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self,item):
        super().add(item)
        self.sort()

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self._validate(x)
        #super().__init__(items)
        s = super()
        ic(s)
        s.__init__(items)
        ic(s.__init__)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only support integer values.')

    def add(self,item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass

if __name__ == '__main__':
    sl = SortedList([4,3, 70, 12])
    ic(sl)
    sl.add(-1)
    ic(sl)
    ic(len(sl))

    il = IntList([1,2,3])
    ic(il)
    il.add(4)
    #il.add('a')
    si = SortedIntList([1,2,3,4, -5 ,-10, -100])
    ic(si)

    s = SortedIntList()
    ic(super(IntList, s).add)
    super(IntList, s).add("I'am not a number! I am a free man")
    ic(s)

