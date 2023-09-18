# pip install icecream

from icecream import ic

def do_stuff():
    some_var = "data"
    some_list = [1,2,3,4]
    ic()
    return some_var

#ic(do_stuff())
do_stuff()

