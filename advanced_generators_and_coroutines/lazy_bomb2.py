class MyNotLazyBomb:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyNotLazyBombIterator(self.number)

class MyNotLazyBombIterator:
    def __init__(self, number):
        self.number = number
        self.squares = {x:x ** 2 for x in range(number)}
        # Notice the dictionary, this is highly optimized!
        # indexing in dicts is highly scalable

        self.index = 0


    def __next__(self):
        try:
            value = self.squares[f'{self.index}']
        except KeyError:
            raise StopIteration
        self.index += 1
        return value


def mylazygenerator(number):
    index = 0
    while index < number:
        yield index ** 2
        index += 1




