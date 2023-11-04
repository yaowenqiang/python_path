"""
itertools.islice()
Perform lazy slicing of any iterator.
"""
from itertools import islice
islice(al_primes, 1000)

"""
itertools.count()
An unbounded arithmetic sequence of integers

from itertools import count, islice

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
list(thousand_primes)[-10:]
sum(islice((x for x in count() if is_prime(x)), 1000))

"""



any([False, True, False])
all([False, True, False])

# any(count()) True
# all(count()) False


from itertools import chain


