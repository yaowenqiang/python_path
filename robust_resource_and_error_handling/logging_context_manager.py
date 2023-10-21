import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield "You're in a with-block"
    except Exception:
        print('logging_context_manager: exceptional exit', sys.exc_info())
        raise


if __name__ == '__main__':
    with logging_context_manager() as x:
        raise ValueError('something went wrong!')
        print(x)
