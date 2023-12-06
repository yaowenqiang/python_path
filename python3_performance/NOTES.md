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
- Worst cases

Performance

Dictionaries

+ Key-value pairs
+ Restrictions on keys
+ Fast access by key - O(1)
+ Fast search

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

Named Tuples

+ Always immutable
+ Tuples, not  classes
+ Memory efficient

> python -m timeit '{"order_id":1}'
> python -m timeit  -s 'from collections import namedtuple; Order=namedtuple("Order", "order_id");Order(1)'
> 
> python -m timeit  -s """
> from dataclasses import dataclass
> @dataclass
> class Order:
>     order_id: int
> """'Order(1)'

> python -m timeit -s 'order={"order_id":1}' 'order["order_id"]'
> python -m timeit -s 'from collections import namedtuple; Order=namedtuple("order", "order_id");order=Order(1)' 'order.or der_id'
> 
> python -m timeit -s  """
> from dataclasses import dataclass
> @dataclass
> class Order:
>     order_id: int
>     order=Order(1)""" 'order.order_id'
>     20000000 loops, best of 5: 17.2 nsec per loop
> """

Functions

How to use Caching

+ Basic approach with dictionaries
+ Caching with @lru_cache
+ Use third party module(joblib)

For loops vs List Comprehensions

For loops

+ More flexibility
+ Better fo adding more logic
+ Lengthy
+ Slower for simple logic

List comprehensions

+ only for creating a new list
+ Great for simple logic
+ Concise
+ Faster for simple logic
+ Set and directory comprehensions

Limitation of Generator Expressions

+ iterate only once
+ No random access

Generator Expression vs List Comprehensions

Generator Expressions

+ ()
+ Less flexible
+ iterate only once
+ Access only next item
+ Very low memory

List comprehensions

+ ()
+ Very flexible
+ iterate many times
+ Access any item
+ High memory

How to concatenate Strings

+ + operator
+ join
+ f-string

Tradeoffs

+ Using + Slow performance, Very friendly, Scalable
+ Using f-string - High performance, friendly, Not Scalable
+ Using join - High performance, Less friendly, Scalable

Permission

Forgiveness

Self-sufficient Function vs Calling Other Functions

Self-sufficient function

+ Duplicate code
+ Less reusable
+ More difficult to maintain
+ Better performance

Calling other functions

+ Clean code
+ More reusable
+ Easier to maintain
+ Slower performance

PYhon inteperter

+ CPython
+ Pypy
+ Jython
+ IronPython
+ Pyston

install Pypy3

```shell
brew install pypy3
```

Threads vs Processes



Threads

+ LIghtweight

+ Shared memory

+ HIgh potential for bugs

+ GIL constaint



Processes



+ Heavyweight

+ Separate memory

+ Low potential for bugs

+ No GIL constraint



Synchronizing Threads



+ Race conditions

+ Deadlocks

+ Starvation

+ Livelocks



Troubleshooting



Global Interpreter lock



+ Only one thread is running

+ The sleep() function releases the GIL

+ Most impact on CPU-intensive tasks



How to synchronize Threads



+ Locks

+ Semaphores

+ Condition variables



When to Use Thread



Use Threads



+ Tasks that wait for external events

+ Blocking I/O

+ simple Logic





Avoid Threads



+ No waiting for external events

+ CPU-intensive tasks

+ Complex logic





Asynchronous Code



Async vs Threads



Async



+ Low overhead

+ Low potential for bugs

+ Learning curve

+ Compatibility constraint



Threads



+ High overhead

+ High potential for bugs

+ Simple syntax

+ High compatibility



Challenges of Working with Asyncio



+ Learning curve
  
  + New syntax: async, await
  
  + New concepts: coroutine , event loop
  
  + New libraries: aiohttp, aiomysql

+ Debugging
  
  + Understand order of executing
  
  + Understand state of application

+ compatibility
  
  + Third-party libraries
  
  + Blocking code
    
    
    
    
    
    
    

When to use Asyncio

+ I/O operations

+ Many small tasks

+ Avoid synchronizing threads

+ Asynchronous dependencies

+ Data processing pipelines

+ Networking applications



When to Avoid Using Asyncio



+ CPU intensive tasks

+ Blocking code

+ Blocking dependencies








