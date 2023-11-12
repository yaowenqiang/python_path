Argument Types

Positional arguments are matched with formal arguments by position, in order

Keyword arguments are matched with formal arguments by name

Arguments may have a default value
The default value for an argument is only evaluated once


Functions are objects and can be passed around just like any other object


__call__()

Allow instances of classes to be callable objects
__call()__ is invoked on objects when they are called like functions

from timeit import timeit
timeit(setup='from __main__ import resolve', stmt='resolve("google.com")', number=1)
print(f"{_:f}")


Class objects and instances of classes are very different things
class binds a class object to a named reference

Arguments passed to the class object are forwarded to the class's __init__()


Alternatives to Class

cls Shortened version 'clsss', Very common in the Python ecosystem
klass Deliberate misspelling of 'class', A bit more explicit

conditional expressions

Evaluates to one of two expressions depending on a boolean

result = true_value if condition else false_value


Functions vs Lambdas

def name(args): body | lambda args: expr

def statement which defines a function and binds it to a name
lambda is Expression which evaluates to a function

function must have a name

lambda is anonymous
function arguments delimited by parentheses, separated by commans,
Lambdas arguments list terminated by a colon, separated by commas

in function zero or more arguments supported - zero argument => empty parentheses
Zero ore more arguments supported in lambda => zero argument => lambda:

function body is an indented block statements
lambda body is a single expression

in function a return statement is required to return anything other than none
in lambda The return value is give by the body expression, no return statement is permitted

Regular functions can have docstrings
Lambdas cannot have docstrings

functions are easy to access for testing
Lambdas are Awkward or impossible to test

Determine Callable objects

> callable(objects)


Rules for * args

+ Must come after normal positional arguments
+ Only collects positional arguments


Arbitrary keyword arguments

prefix argument with ** to accept arbitrary keyword arguments
Conventionally called **kwargs



Positional-only Arguments


dict() use **kwargs in its initializer


Argument Forwarding




Local functions

local functions are function defined in function,defined when def is executed
new copy made for each enclosing invocation
Separate name binding each time

Scope Rules

+ Local
+ Enclosing
+ Global
+ Built-in


Name resolution for local functions

Starts with names in the local function
Then checks enclosing scope(s)
Finally module-level and built-in names are checked

Local functions are not 'members' of their enclosing functions


First-class functions

Functions can be passed to and returned from functions
More generally, they can be treated like any other data
A powerful concept that becomes even more powerful when combined with closures


How does a returned local function retain access to its enclosing scope?

Once the local functions is returned ,the enclosing scope is gone!

How can the returned local function continue to operate?

Closure

Records objects from enclosing scopes
Keeps recorded objects alive for use after the enclosing scope is gone

implemented with the __closure__ attribute


Function factory

Functions that return other functions

Returned functions use both their own arguments as well as arguments to the factory
Combination of runtime function definition and closures


Binding names in enclosing scopes

global

introduces binds from the global scope into another scope
We can bind the global message into local()


How can we bind names from enclosing scopes?

How can we make local() modify the binding in enclosing?

nonlocal

Insert a name binding from an enclosing scope into the local namespace
Searches enclosing scopes from innermost to outermost
use the first match found


Decorators

Modify or enhance an existing function in a non-intrusive and maintainable way
implemented as a callable that accepts a callable and returns a callable

"A function accepting a function and return a function"

@my_decorator
def my_function():

Decorators allow you to modify existing functions without changing their definition
Callers don't need to change when decorators are applied

Classes as Decorators

classes are callable objects
Functions decorated with a class are replaced by an instance of the class
These instances must themselves be callable

We can decorate with a class as long as instances of the class implement __call__()

Instances as decorators

Python call an instance's __call__() when it's used as a decorator
__call__()'s return value is used as the new function'
Create groups of callables that you can dynamically control as a group

Multiple decorators

@decorator1
@decorator2
@decorator3
@decorator4
def some_function():

Callable Metadata

We can copy __name__ and __doc__ from our wrapped function to our wrapper function

functools.wraps()
Replace decorator metadata with that of the decorated callable.
It's a decorator that you apply to your wrapper function
It does the hard work for you!

map()

calls a function for the elements in a sequence, producing a new sequence with the return values
It 'maps' a function over a sequence
Map() is Azay
map() will not call its function or access its iterables until they're needed for output
A map object it itself iterable, iterate over it to produce output

map() vs. Comprehensions

Performance

Neither map() or Comprehensions are necessarily faster than the other

Readability

Some people find one form more readable then the other

Context

the choise between the two will often depend on your specific context.


filter()

Removes elements from a sequence which don't meet some criteria
Applies a predicate function to each element
Produces its results lazily
Only accepts a single input sequence, and the function must accept only one element

filter(function, sequence)

Passing None as the first argument to filter() will filter out input elements which evaluate to False

map() and filter() behave differently in Python 2 and Python 3

In Python3 they are lazy
In Python2, they are eager and return lists


functools.reduce()

Repeatedly applies a two-argument function to an accumulated value and the next element from a sequence
The initial value can be the first element in the input sequence or an optional argument
The final accumulated - or reduced - value is returned

reduce() is not unique to Python

fold() in many functional language

Aggregate() in .NET's LINQ
accumulate() in C++'s Standard Template Library
reduce() accepts an optional initial value
Conceptually added to the start of the sequence
Served as the first accumulator value.

map-reduce


Multi-input Comprehensions

Comprehensions can have multiple input iterables and if-clauses.
You can have multiple if-clauses in a Comprehensions as well
Later clauses are nested inside earlier clauses





