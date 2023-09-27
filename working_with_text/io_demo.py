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

from icecream import ic
ic(open('foo.txt', 'rt'))
ic(open('foo.txt', 'rb'))
ic(open('foo.txt', 'rb', buffering=0))
