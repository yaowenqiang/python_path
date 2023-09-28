"""
I/O classes
FileIo
BufferedReader
BufferedWriter
BufferedRWPair
BufferedRandom
TextIOWrapper
BytesIO
StringIO

"""
import codecs
import sys
import io
from urllib.request import urlopen

from icecream import ic
ic(open('foo.txt', 'rt'))
ic(open('foo.txt', 'rb'))
ic(open('foo.txt', 'rb', buffering=0))

for line in open('foo.txt', encoding='utf-8'):
    pass
for line in codecs.open('foo.txt', encoding='utf-8'):
    pass

# sys.stdout.write(b'Hello World\n')
sys.stdout.buffer.write(b'Hello World\n')

u = io.TextIOWrapper(
    urlopen('https://www.python.org'),
    encoding='utf-8'
)
text = u.read()
ic(text)



u = io.TextIOWrapper(
    urlopen('https://www.python.org'),
    encoding='utf-8'
)
line = u.readline()
ic(line)
