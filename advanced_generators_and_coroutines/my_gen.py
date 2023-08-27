import inspect
def generator():
    yield 'I am a generator'
    yield 'And i count'
    yield 1
    yield 2
    yield 'I am thinking the next one'
    yield 3

mygen = generator()
next(mygen)

inspect getgeneratorstat(mygen)
