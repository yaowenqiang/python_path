def lucas():
    yield 2
    a = 2
    b = 1
    whileTrue:
        yield b
        a, b = b, a + b


