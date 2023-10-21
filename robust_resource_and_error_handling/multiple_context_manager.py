import contextlib
# with cm1() as a, cm2() as b:
    # body

#with cm1() as a:
#    with cm2() as b:
#        body


@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield name
    print('Exiting', name)

@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception.')
        if propagate:
            raise


if __name__ == '__main__':
    with nest_test('outer') , nest_test('inner'):
        print('BODY')

    with nest_test('outer') as n1, nest_test('inner nested in ' + n1):
        print('BODY')

    with propagater('outer', True), propagater('inner', False):
        raise TypeError()

    with propagater('outer', False), propagater('inner', True):
        raise TypeError()
