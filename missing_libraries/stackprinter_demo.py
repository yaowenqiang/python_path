# pip install stackprinter

import stackprinter

stackprinter.set_excepthook(style='darkbg2')

def do_stuff():
    some_var = "data"
    raise ValueError("Some erro message")

do_stuff()
