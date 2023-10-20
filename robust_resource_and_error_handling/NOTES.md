>>> IndexError.__mro__ (IndexError, LookupError, Exception, BaseException, object)
>>> KeyError.__mro__ (KeyError, LookupError, Exception, BaseException, object)

# Python Exception Hierarchy

> https://martinxpn.medium.com/exception-hierarchy-python-58-100-days-of-python-9d8585e6569b

use Python's -O argument to turn on basic optimization
in particular, this flag disables assertions


>  python -O


python -m timeit -s "from random import randrange; from sorted_set import SortedSet; s = SortedSet(randrange(1000)for _ in range(2000))" "[s.contains(i) for i in range(1000)]"
> 1 loop, best of 5: 64.4 msec per loop
>
python -O -m timeit -s "from random import randrange; from sorted_set import SortedSet; s = SortedSet(randrange(1000) for _ in range(2000))" "[s.contains(i) for i in range(1000)]"
> 1 loop, best of 5: 294 usec per loop
>

