import numpy

def double_list(size):
    initial_list = list(range(0, size))
    return [2 * i for i in initial_list]

def double_array(size):
    initial_array = numpy.arange(size)
    return 2 * initial_array

double_list(1_000_000)
double_array(1_000_000)
