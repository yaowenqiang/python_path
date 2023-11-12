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




