import dis
def countdown(n):
    while n > 0:
        print n
        n -= 1

dis.dis(countdown)
