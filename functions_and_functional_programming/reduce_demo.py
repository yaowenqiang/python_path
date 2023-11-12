from functools import reduce
import operator
numbers = [1,2,3,4,5]
reduce(operator.add, numbers)
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accmulator = operator.add(accumulator, item)

print(accumulator)

def mul(x,y):
    print(f'mul {x} {y}')
    return x * y

print(reduce(mul, range(1,10)))
#reduce(mul, []) TypeError
reduce(mul, [1]) # won't call the mul reduce function

values = [1,2,3]
reduce(operator.add, values, 0)

values = []
reduce(operator.add, values, 0)

values = [1,2,3]
reduce(operator.mul, values, 1)

