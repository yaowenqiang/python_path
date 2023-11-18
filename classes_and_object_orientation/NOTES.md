Class Attribute Syntax

class Myclass:

myclass_attribute = 'calss attributes go here'
MY_CONSTANT = 'they are often class-specific contants'

def __init__(self):
    self.my_instance_attribute = 'instance attributes go here'


Scopes in Python

Local Inside the current function
Enclosing Inside enclosing functions
global At the top level ofthe module
Built-in In the special builtins modules

LEGB

Choosing

@classmethod

Requires access to the class object to call other class methods or the constructor

@staticmethod

No access needed to either class or instance objects()
Most likely an implementation detail of the class

May be able to be moved outside the class to become a global-scope function in the module


The 'named constructor' idiom

A factory method which returns an instance of a class.The method name allows callers to express intent, and allows construction to be performed with different combination of arguments.

Originally a C++ idiom, also applicable in Python

For polymorphic dispatch invoke static methods through self.

Use **kwargs to threadarguments throught named-constructor class-methods to more specialized subclasses.

Don't override properties directly, Delegate to regular methods and override these instead


Conversitions for Good __repr__ Results:

include necessary state, but be prepared to compromise
format as constructor invocation source code



str

str(obj)

str(object) invoks obj.__str__() -> 

object.__str__ invokes__repr__

# Base class initialization

If a class uses multiple inheritance and defines no initializer, only the initializer of the first base class is automatically called.


__bases__


Method Resolution Order


Ordering of an inheritance graph that determines which implementation to use when invoking a method

Method implementation may be found in any class in an inheritance graph

Determines the order in which the graph is searched when looking for an implementation


__mro__


How is MRO Used?

Python finds the MRO for the type of the object on which a method is invoked
Python checks each class in MRO in order to find one that implements the method
The first implementation found is used


object

the ultimate base class for every class in Python.


Calculating Method Resolution Order

C3 
Algorithm used to calculate method resolution orders.

Ensures that :
    Subclasses come before base classes
    Bass class order from class defination is preserved
    The first two qualities are preserved for all MROs in a program

C3 prohibits some inheritance declarations on Python.


super()

Given a method resolution order and a class C in that MRO, super() gives you an object which resolves methods using only the part of the MRO which comes after C.
super() works with the MRO of an object, not just its base classes.

super() gives you a proxy object
the proxy resolves the correct implementation if any requested method
It has access to the entire inheritance graph of the object

super() uses the full MRO of an object, not just the base classes from a class defination

class-bound Super Proxies


What happens if you use super() in a classmethod?

We don't have an instance to work with, but we do have a class object.

super() derives the MRO from the class object rather than the type of self.

Explicit Arguments to super(0)

super(class-object, instance-or-class)

Duck typing

In Python, the type of an object doesn't determine if it can be use in a particular context.
Ptyon uses duck typing where fitness for purpose is determined at the time of use.
Functions don't specify their types.
you can call any method on any object, and Python won't complain until runtime.


Data class
'''python
@dataclass(
init=True,
repr=True,
eq=True,
order=False,
unsafe_hash=False,
frozen=False,
)
class MyDataClass:
    fred: int
    jim: int
    sheila: int
'''

Prefer immutable Dataclasses

Use immutable attribute types

Declare the dataclass as frozen(immutable)

def __post_init__(self):
    if self.fred < 0:
        raise ValueError




