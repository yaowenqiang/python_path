# __traceback__
import math
from icecream import ic
from traceback import print_tb, format_tb

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
        print(e.__traceback__)
        print_tb(e.__traceback__)
        ic(format_tb(e.__traceback__))

    ic('Finished!')
