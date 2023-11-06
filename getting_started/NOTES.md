float

IEEE-754 double-precision with 53-bites of binary precision



# PEP 278

universal newlines 

# raw strings 

path = r'c:\windows\system32'


wegian unicode characters


Python Execution Model

Python module

> Convenient import with API

Python script

> Convenient execution from the command line

Python Program 

> Perhaps composed of many modules

Command line arguments 


+ sys.argv
+ dotopt module
+ argparse module


Docstrings PEP 257

sphinx


google python style guide
> https://google.github.io/styleguide/pyguide.html


Pylauncher
PEP 397

def is a statement execute at runtime
default arguments are evaluated when def is executed
immutable default value don't cause problems
Multable default values can cause confusing effects

always use immutable objects for default values.

## Scopes in Python

+ Local Inside the current function
+ Enclosing Inside enclosing functions
+ Global At the top level of the module
+ Built-in In the special builtins module

LEGB Rule


## strings

Use str.join() to join strings

+ Concatenation with + results in temporaries
+ str.join() inserts a separator between a collection of strings
+ Call join() on the separator string


PEP 498: Literal String interpolation
commonly called f-strings

help(str)

## range

+ range(stop)
+ range(start,stop)
+ range(start,stop, step)

### enumerate

Constructs an iterable of (index, value) tuples around another iterable object

### deep copy use the copy module


## sets


union
difference
symmetric_difference
intersection
subset
superset
disjoint



#3 Protocols

Protocol | Implenting collections
-------- |  ------------------- |
Container | str, list, dict, range, tuple, set ,bytes (in or not in)
Sized | str, list, dict, range, tuple, set ,bytes (len)
Iterable | str, list, dict, range, tuple, set ,bytes (Yield items one by one as they are requested)
Sequence | str, list, range, tuple, bytes( item = sequence[index] , i = sequence.index[item], num = sequence.count(item), r = reversed(sequence))
Multable Sequence | list
Multable Set | set
Multable Mppping | dict


LBYL vs EAFP

Look Before You leap

Easier to ask forgiveness then permission
Python prefers EAFP

Platform-specific modules

On Windows:
msvcrt
On Mac or Linux:
tty,termios, sys


### Iteraction Protocols

+ iterable - can be passed to iter() to produce an iterator
+ iterator - Can be passed to next() to get the next value in the sequence


late binding

get system default encoding

import sys
sys.getdefaultencoding()

> https://docs.python.org/library/codecs.html#standard-encodings

Seek cannot move to arbitrary offset.Only 0 and values from tell() are allowed, Other values result in undefined behavior.

use sys.stdout.write() instead of print ,This won't add newliens like print()



Expansion of the with-block

mgr = (EXPR)
exit = type(mgr).__exit___
value = type(mgr).__enter__(mgr)
exc = True
try:
    try:
        var = value
        block
    except:
        exc = False
        if not exit(mgr, *sys.exc_info())
        raise
    finally:
        if exc:
            exit(mgr, None, None, None)
