import itertools
class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap

map(ord, 'the quick brown fox')

result = map(Trace()(ord), 'the quick brown fox')
print(result)
next(result)
list(result)
for i in result:
    print(i)

sizes = ['small', 'medium', 'large']
colors = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus','salamander']
def combine(size, color, animal):
    return f'{size} {color} {animal}'
print(list(map(combine, sizes, colors, animals)))

def combine_inf(quantity, size, color, animal):
    return f'{quantity} x  {size} {color} {animal}'

print(list(map(combine_inf, itertools.count(), sizes, colors, animals)))

[str(i) for i in range(5)]
list(map(str, range(5)))
(str(i) for i in range(5))

