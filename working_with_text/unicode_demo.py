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
for i in s:
    ic(ascii(ic(i)))

