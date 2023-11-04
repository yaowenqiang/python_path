import sys
from math import log

DIGIT_MAP = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

def convert(s):
    try:
        number = ''
        for token in s:
            number += str(DIGIT_MAP[token])
        return int(number)
    except (KeyError, TypeError) as e:
        print(f'Conversion error: {e!r}', file=sys.stderr)
        #return -1
    raise 

def string_log(s):
    v = convert(s)
    return log(v)


if __name__ == '__main__':
    s = convert('one two three'.split())
    print(s)
    print(string_log('one two three ten'.split()))
