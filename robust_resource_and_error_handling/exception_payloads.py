from icecream import ic
def median(iterable):
    items = sorted(iterable)
    if len(items) == 0:
        # only a single string argument should be used
        # PEP 352
        raise ValueError('median() arg is an empty series!')
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]

    return (items[median_index] + items[median_index + 1]) / 2

if __name__  == '__main__':
    arr  = [1,2,3,4,5]
    ic(median(arr))
    try:
        ic(median([]))
    except ValueError as e:
        ic("Payload: ",e.args)
        print("Payload repr : ",repr(e.args))
        print("Payload: str: ",str(e.args))
