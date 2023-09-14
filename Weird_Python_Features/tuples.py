some_tuples = ([1], [2])
print(id(some_tuples))
some_tuples[0].append(2)
print(some_tuples)
# ([1, 2], [2])
some_tuples += ([3],)
print(id(some_tuples))
# two ids is  different

x = ([1,2], )
try:
    x[0] += [3,4]
except Exception as e:
    print(e)

print(x)
