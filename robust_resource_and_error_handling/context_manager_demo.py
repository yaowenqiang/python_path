# PEP 343
# https://peps.python.org/pep-0343/

class LogginContextManager:
    def __enter__(self):
        print('LogginContextManager.__enter__()')
        return "You are in a with-block!"
        #return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LogginContextManager.__exit__: ', 'Normal exit detected')
        else:
            print('LogginContextManager.__exit__:'
                  'Exception detected! ',
                  f'type = {exc_type}, value={exc_val}, traceback={exc_tb}'
                  )


if __name__ == '__main__':
    with LogginContextManager() as x:
        raise ValueError('Something has gone away!')
        print(x)
