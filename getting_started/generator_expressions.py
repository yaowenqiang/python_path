"""
 (expr(item) for item in iterable)
 """

million_sequares = (x*x for x in range(1, 1000001))
list(million_sequares[-10:])

sum(x*x for x range(1, 1000001))
sum(x*x for x range(1, 1000001) if is_prime(x))
