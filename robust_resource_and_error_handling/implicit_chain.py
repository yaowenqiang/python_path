import math
import sys
import io

class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return f'{self.args[0]} for sides {self._sides}'

    def __repr__(self):
        return f'TriangleError({self.args[0]!r}, {self._sides!r})'

    pass

def triangle_area(a,b,c):
    sides = sorted((a,b,c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError('Illegal triangle',sides)
    p = (a + b + c) / 2
    a = math.sqrt(p*(p-1)*(p-b)*(p-c))
    return a

if __name__  == '__main__':
    try:
        a = triangle_area(3,40, 10)
        print(a)
    except TriangleError as e:
        try:
            print(e, file=sys.stdin)
        except io.UnsupportedOperation as f:
            print(e)
            print(f)
            print(f.__context__ is e)
