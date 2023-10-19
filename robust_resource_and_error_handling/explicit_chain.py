import math

class InclinationError(Exception):
    pass

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError('Slope cannot be vertical!') from e

if __name__  == '__main__':
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e)
        print(e.__cause__)
    # __cause__
