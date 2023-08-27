 Equivalent to for i in x: print(x)!

 x = [1,2,3,4]
 _x = iter(x)
 next(_x)


> An iterator is any object that you can fetch the next element from it, via the special method __next__

> an iterable is any object that via a special method called __iter__ it can get an iterator


Generators features

+ Lazy
+ Performant
+ Asynchronous

ipython:
from lazy_bomb import *
%timeit for _ in MyNotLazyBomb(10000): True
%timeit  for _ in mylazygenerator(10000): True

> pip install memory_profiler

> %load_ext memory_profiler
%memit for _ in MyNotLazyBomb(10000): True
%memit  for _ in mylazygenerator(10000): True

%memit for _ in MyNotLazyBomb(100000000): True
%memit for _ in mylazygenerator(100000000): True

## Generators Expressions

```python
    for i in s:
        if condition:
            yield expression
```
> (expression for i in s if condition)
> for i in mylazygenerator(5):
>   print(f'----> {i}')

for i in (x**2 for x in range(5)):
    print(f'---> {i}')

> https://www.dabeaz.com/generators/Generators.pdf
