vals = [[y * 3 for y in range(x)] for x in range(10)]

outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)

{x * y for x in range(10) for y in range(10)}
g = ((x,y) for x in range(10) for y in range(x))
