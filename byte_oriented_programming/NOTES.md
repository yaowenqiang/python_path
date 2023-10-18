# Bitwise Operators

+ Bitwise-and &
+ Bitwise-or |
+ Bitwise-xor ^
+ Complement ~
+ Left-shift <<
+ Right-shift >>

0b1111000
bin(240)

0b10101010 & 0b11001100

> Nybbles

bin(
    0b1100 &
    0b1010).rjust(9)

## Masking 

Masquerade() ball goers partially hide faces with masks

Masking with Bitwise-and


bin(
    0b110111000001010000111100 &
    0b111111110000000000000000).rjust(29)

Right shift >> 

Shifts a given number of bits to the right

0b1010 >> 1

hex(0b110111000001010000111100)
hex(0b111111110000000000000000)

hex(
    0xdc143c &
    0xff0000
).rjust(11)

hex((
    0xdc143c &
    0xff0000
)>> 16).rjust(11)

bin(0b11111111 << 16)
hex(0xff << 16)
hex(0xff << 8)
hex(0xff << 0)

hex((
    0xdc143c &
    0xff << 8
) >>  8)

Numbering in Bitfields

import stat
stat.S_IXOTH # 1
stat.S_IWOTH # 2
stat.S_IROTH # 4

stat.S_IXGRP # 8
stat.S_IWGRP # 16
stat.S_IRGRP # 32

stat.S_IXUSR # 64
stat.S_IWUSR # 128
stat.S_IRUSR # 256

