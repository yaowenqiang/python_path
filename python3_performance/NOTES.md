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
