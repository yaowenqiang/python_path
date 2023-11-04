import time
from icecream import ic
print(time.ctime())

def show_default(arg=time.ctime()):
    print(arg)

def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

show_default()
show_default()
show_default()
show_default()

breackfast = ['bacon', 'eggs']
add_spam(breackfast)
ic(breackfast)
launch = ['baked beans']
add_spam(launch)
ic(launch)

## Scopes in Python

+ Local Inside the current function
+ Enclosing Inside enclosing functions
+ Global At the top level of the module
+ Built-in In the special builtins module

LEGB Rule


