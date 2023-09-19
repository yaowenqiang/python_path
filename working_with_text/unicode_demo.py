from icecream import ic
t = "That's a spycy Jalape\u00f1o!"
print(t)
a = '\xf1'
b = '\u210f'
c = '\U0001d122'
ic(a)
ic(b)
ic(c)
