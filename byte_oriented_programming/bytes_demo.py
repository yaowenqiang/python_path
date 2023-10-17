def bytes_at(v, n):
    s = n * 8
    return (v & (0xff << s)) >> s

crimson = 0xdc143c

def rgb(color):
    return (
        bytes_at(color, 2),
        bytes_at(color, 1),
        bytes_at(color, 0),
    )
print(rgb(crimson))
