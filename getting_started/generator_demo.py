from icecream import ic
def gen123():
    yield 1
    yield 2
    yield 3

def gen246():
    ic('about to yield 2')
    yield 2
    ic('about to yield 4')
    yield 4
    ic('about to yield 6')
    yield 6
    ic('about to return')

g = gen123()
ic(next(g))
ic(next(g))
ic(next(g))
#ic(next(g))
g = gen246()
ic(next(g))
ic(next(g))
ic(next(g))
ic(next(g))

