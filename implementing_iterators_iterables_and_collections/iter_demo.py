# iterable

class MyIterable:
    def __iter__(self):
        iterator = MyIterator(self)
        return iterator

class MyIterator:
    def __iter__(self):
        return self

    def __next_-(self):
        if not has_more_items():
            raise StopIteration
        item = get_the_next_item()
        return item

if __name__ == '__main__':
    iterator = iter(iterable)
    item = next(iterator)

