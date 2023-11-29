Measure Performance with Python

+ Use the time() function
+ Use the timeit module
+ Use the pytest-benchmark plugin for pytest


> python -c 'for _ in range(100_100_100): pass'
> time python -c 'for _ in range(100_100_100): pass'
> python -m timeit  'for _ in range(100_100_100): pass'
> pip install pytest-benchmark
> pytest


Type of Profiling

+ Event-based or deterministic
  + Gather data on events
  + Lots of data
  + High accuracy
  + High overhead
+ Statistical
  + Sampling the program
  + Less data
  + Approximation
  + Less overhead


Profiling Modules included in Python

+ The profile module 
  + Adds significant overhead 
  + easy to extend
+ The cProfile Module
  + Adds overhead
  + General purpose

> python -m profile file.py
> python -m cCrofile file.py

Limitations of Integrated Profiles

+ Performance
+ Can't not profile Multithreading
+ Visibility inside functions 
+ Memory visibility


Third-party profilers

+ Line_profiler
+ Py-spy
+ Scalene
+ Yappi
+ Memory_profiler


> pip install line_profiler
> add @profiel to function
> kerprof -lv filapath.py

> pip install memory_profiler
> python -m memory_rofiler  memory_profiler.py

Plotting with memory_profile

> pip install matplotlib
> mprof file.py
> mprof plot --output file.jpg

Visualizing Profile Data with Snakeviz

Visualize cProfile output
Browser-based

> pip install snakeviz
> python -m cProfile -o file.prof file.py
> snakeviz file.prof

Visualizing Profiling Data file>with PyCharm Professional

View call graph
+ Red for high consumers
+ Green for low consumers


List Performance

Very fast - O(1)

+ Getting
+ Setting
+ Appending


Slow- O(n)

+ Finding
+ Removing


Memory allocation

- Extral room for future appends
- Old list is copied to the new list
-

Arrays

Built-in arrays

+ compact data storage
+ Only for certain types 
+ less popular


NumPy arrays

+ Numeric computations
+ iterms of different types
+ Very popular
+
> python -m cProfile -o list_array.prof list_arrays.py
> snakeviz list_array.prof

Sets performance

Very fast -O(1)

+ Adding
+ Deleting
+ Membership checking


Slow - O(n)



Sets vs Tuples

Sets

+ Mutable
+ Unordered collection
+ Unique, immutable items
+ Fast membership-check
+ Sets-specific operations


Tuple

+ immutable
+ Ordered collection
+ Fixed content
+ Memory efficient


> python -m memory_profiler set_tuple.py
> kernprof -lv set_tuple.py

Python Queue Implementations

Queue vs Deques

Queue

+ From queue module
+ Simple queue
+ First-in-First-Out
+ Specialized for multithreading
+ Few operations

Dequeues

+ From collections module
+ Double-ended queue
+ FIFO, Last-~n-First-Out
+ Multithreading support
+ More operations
+

Performance

Dequeues vs Lists

Dequeues

+ Slow access by index - ((n))
+ Fast append and pop at the end
+ Fast append and pop at the start


Lists

+ Fast access by index - O(1)
+ Fast append and pop at the end
+ Slow append and pop at the start

+ Dictionary Performance
+
+ Very fast - O(1)
+ Getting 
+ Setting
+ Deleting
+
Slow - O(n)
  - Worst cases
  -


Performance

Dictionaries

+ Key-value pairs
+ Restrictions on keys
+ Fast access by key - O(1)
+ Fast search
+

Lists

+ Individual items
+ No restrictions
+ Fast access by index - O(1)
+ Slow search

Named Tuples vs Data Class

Data Class 

+ Multable by default
+ Supports class features
+ Fast access
+

Named Tuples

+ Always immutable
+ Tuples, not  classes
+ Memory efficient


> python -m timeit '{"order_id":1}'
> python -m timeit  -s 'from collections import namedtuple; Order=namedtuple("Order", "order_id");Order(1)'
>
> python -m timeit  -s """
from dataclasses import dataclass
> @dataclass
class Order:
    order_id: int
"""'Order(1)'

> python -m timeit -s 'order={"order_id":1}' 'order["order_id"]'
> python -m timeit -s 'from collections import namedtuple; Order=namedtuple("order", "order_id");order=Order(1)' 'order.or der_id'
>
> python -m timeit -s  """
from dataclasses import dataclass
@dataclass
class Order:
    order_id: int
    order=Order(1)""" 'order.order_id'
    20000000 loops, best of 5: 17.2 nsec per loop
> """
