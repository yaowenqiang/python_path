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
import glob
from urllib.request import urlopen
import base64

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


f = open("jalape\xf1o.txt","a")
f.write('Bwahahahaha!\n')
f.close()

u = io.TextIOWrapper(
    urlopen('https://www.python.org'),
    encoding='utf-8')
line = u.readline()
ic(line)

#f = open(b"jalape\xf1o.txt","a")
files = glob.glob(b'*.txt')
ic(files)
files = glob.glob('*.txt')
for file in files:
    print(file)

data = b'Hello World'
base64.b64encode(data)
ic(base64.b64encode(data))
s = bytes('jalapeño.txt', 'utf-8')
ic(base64.b64encode(s))
