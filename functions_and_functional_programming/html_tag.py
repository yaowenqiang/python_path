def _tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

def tag(name, **attributes):
    result = '<' + name
    for k, v in attributes.items():
        result += f' {k}="{v}"'
    result += '>'
    return result


def name_tag(first_name, last_name, *, title=''):
    print(title, first_name, last_name)

#def print_args(**kwargs, *args): not allowed
#    pass

def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

def print_kargs(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)

def print_karg(first_name, last_name, *, title=''):
    print(title, first_name, last_name)


def print_arg_and_karg(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


# since python 3.8

def number_length(x, /):
    return len((str(x)))

# number_length(x=1) # error, 
# name_tag('judy', 'spudmeyer', title='galactic commander')
# name_tag('judy', 'spudmeyer','kirk'  title='galactic commander') # wrong, 

