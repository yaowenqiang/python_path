import sys
from timeit import timeit
from icecream import ic
t = "That's a spycy Jalape\u00f1o!"
ic(t)
a = '\xf1'
b = '\u210f'
c = '\U0001d122'
d = '你'
ic(a)
ic(b)
ic(c)
ic(ascii(a))
ic(d)
ic(ascii(d))
ic(d)
s = 'Jalape\xf1o'
d = 'Jalapen\u0303o'
# https://www.compart.com/en/unicode/combining/230
ic(s)
ic(d)
ic(s == d)
a1 = 'a\u0303'
a2 = 'a\u0341'
a1 = 'a\u0303'
a1 = 'a\u0300'
s = 'āáǎàōóǒòêēéěèèīíǐìūúǔǔǖǘǚǜü'
prefix = '\u0303'
for i in s:
    ic(ascii(ic(i)))
ic(sys.maxunicode)
ic(a1)
ic(len(a1))
ic(sys.getsizeof(a1))
ic(len(a1))
ic(sys.getsizeof(a1))
ic(len(prefix))
ic(sys.getsizeof(prefix))
ic(timeit('text[:-1]', "text='x'*100000"))
ic(timeit('text.upper()', "text='x'*1000"))
