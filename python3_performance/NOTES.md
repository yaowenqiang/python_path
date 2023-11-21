Measure Performance with Python

+ Use the time() function
+ Use the timeit module
+ Use the pytest-benchmark plugin for pytest


> python -c 'for _ in range(100_100_100): pass'
> time python -c 'for _ in range(100_100_100): pass'
> python -m timeit  'for _ in range(100_100_100): pass'
> pip install pytest-benchmark
> pytest
