from icecream import ic
l = [i * 2 for i in range(10)]
d = {i: i * 2 for i in range(10)}
s = {i for i in range(10)}
g = (i for i in range(10))

[(x, y) for x in range(5) for y in range(5)]

points =  []

for x in range(5):
    for y in range(5):
        points.append((x, y))


values = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x -y != 0]

#ic(values)
values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]
ic(values)

values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x -y != 0:
                values .append(x / (x - y))
#ic(values)

[(x,y) for x in range(10) for y in range(x)]

result = []
for x in range(10):
    for y in range(x):
        result.append((x,y))

