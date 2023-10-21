from bisect import bisect_left


class SortedSet:
    def __init__(self, xs):
        self._set = []
        for x in xs:
            self.add(x)

    def add(self, x):
        self._set.append(x)
        self._set = sorted(set(self._set))
        assert self.is_unique_and_sorted()

    def contains(self, x):
        assert self.is_unique_and_sorted()
        index = bisect_left(self._set, x)
        return index != len(self._set) and self._set[index] == x

    def is_unique_and_sorted(self):
        return all(self._set[i] < self._set[i + 1] for i in range(len(self._set) - 1))


if __name__ == '__main__':
    s = SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert s.contains(10)
