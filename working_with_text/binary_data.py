from icecream import ic
a = b'ACME 50 91.10' # Byte string literal
ic(a.split())
ic(a.lower())
ic(a[5:7])
ic(a)
# a[0] = b'e' bytes are immutable like strings

b = bytes([1,2,3,4,5]) # From a list of integers
ic(b)
c = bytes(10) # An array of 10 zero-bytes
ic(c)
d = bytes("Jalapeño", 'utf-8')
ic(d)
e = bytes.fromhex('48656c6c6f')
ic(e)
# bytes are array of integers
ic(a[0])
for i in a:
    ic(i)
# Conversion of objects into bytes
x = 7
ic(bytes(x))
ic(str(x).encode('ascii'))

# bytearray objects
# a bytearray is a multable bytes objects
s = bytearray(b'ACME 50 91.10')
ic(s)
s[:4] = b'PYTHON'
ic(s)
s = bytearray(b'PYTHON 50 91.10')
s[0] = 0x70
ic(s)
s.append(23)
ic(s)
ic(0x23.to_bytes())
s.append(45)
ic(s)
s.extend([1,2,3,4])
ic(s)
num = 12345
ic(num.to_bytes(2, 'big'))
