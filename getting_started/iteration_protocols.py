from icecream import ic
iterable = ['Spring', 'Summer', 'Autumn', 'winter']
iteraber = iter(iterable)

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('iterable is empty')
ic(next(iteraber))
ic(first(['1st', '2end', '3rd']))
ic(first({'1st', '2end', '3rd'}))
ic(first({}))
ic(first(set()))

