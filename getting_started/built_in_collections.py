k = (123,)
print(k)
k = (123)
print(k)
e = ()
print(e)
b = 1,2,3
print(b)

def minmax(items):
    return min(items), max(items)

min, max = minmax([83,33,3,333,333,44])
print(min)
print(max)


# tuple unpacking
(a,(b,(c,d))) = (4,(3, (2,1)))

a = 'Jelly'
b = 'Bean'
print(a,b)
a,b = b,a
print(a,b)
