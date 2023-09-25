import sys
from timeit import timeit
from icecream import ic
from rich.traceback import install
from string import Template
install(show_locals=True)
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
x = 42
format(x, 'd') # decimal
format(x, 'f') # Floating point
format(str(x), 's') # String
format(x, 'e') # Scientific notation
format(x, 'x') # Hexadecimal
format(x, 'o') # Octal
format(x, 'b') # Binary
format(x, '%') # Percent
y = 2.71828
# [width][.precision]code
format(y, '0.2f')
# Alignment Modifiers
# [<|>|^][width][.precision]code
format(y, '<20.2f') # align left
format(y, '>20.2f') # align right
format(y, '^20.2f') # align middle
# Fill Character
# [fill][<|>|^][width][.precision]code
d = 42
format(d, '08d')
format(d, '032d')
format(d, '=^23d')

# Thousands Separator
# [fill][<|>|^][width][,][.precision]code
x = 123456789
ic(format(x, ',d'))

ic('{:10s} {:#^10d} {:10.2f}'.format('ACME', 50, 91.1))
ic('<{0}>{1}<{0}>'.format('para', 'Hey there'))

# format example

# Positional
# '{0} has {1} messages'.format('Dave', 37)
# Keyword
# '{name} has {n} messages'.format(name='Dave', n=37)
# In order
# '{} has {} messages'.format('Dave', 37)

# String templates

msg = Template('$name has $n messages')
ic(msg.substitute(name="Dave", n=37))
msg = '{name} has {n} messages'
ic(msg.format(name="Dave", n=37))

record = {
    "name": "Dave",
    'n': 37
}

class Record:
    def __init__(self, name, n):
        self.name = name
        self.n = n

ic('{r[name]} has {r[n]} messages'.format(r=record))

record = Record("Dave", 37)
ic('{r.name} has {r.n} messages'.format(r=record))

# {item} # replace by str(item)
# {item!r} # replace by repr(item)
# {item:fmt} # replace by format(item, fmt)

ic('{name:10s} {price:10.2f}'.format(name="ACME", price=91.1))
#ic('{s.name:10s} {s.price:10.f}'.fomrat(s=stock))
ic('{name!r} {price}'.format(name='ACME', price=91.1))
ic('{name} {price}'.format(name='ACME', price=91.1))
ic('The value is {{{0}}}'.format(42))
s = ('ACME', 51, 91.10)
ic('{0:{width}s} {2:{width}.2f}'.format(*s, width=12))
ic('{0:10s} {2:10.2f}'.format(*s))
ic('{0:10s} {1:10.2f}'.format(*s))
ic(f'{s[0]:10s} {s[1]:10.2f}')


# format a mapping

record = {
    'name': 'Dave',
    'n': 10
}

ic('{name} has {n} messages'.format_map(record))
