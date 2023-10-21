@contextlib.contextmanager
def my_context_manager():
    # <ENTER>
    try:
        yield [value]
        # <NORMAL EXIT>
    except:
        # <EXCEPTIONAL EXIT>
        raise

with my_context_manager() as x:
    # ...
