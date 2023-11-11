from icecream import ic
def check_non_negative(index):
    ic(index)
    def validator(f):
        ic(f)
        def wrap(*args):
            ic(args)
            if args[index] < 0:
                raise ValueError(
                    f'Arguments {index} must be non-negative.'
                )
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value,size):
    return [value] * size

print(create_list('a', 3))
