from functools import reduce
from itertools import filterfalse

def calculate_max_until_now(endpoint_map, logline):
    try:
        if logline[9].strop('-\n') != '':
            endpoint_map[logline[5]]['count'] += 1.0
            endpoint_map[logline[5]]['average'] = float(
                (endpoint_map[logline[5]]['average'] * endpoint_map[logline[5]]['count']
                + float(logline[9]) * (endpoint_map[logline[5]]['count'] - 1)) / 
                (
                    endpoint_map[logline[5]]['count'] *
                    (endpoint_map[logline[5]]['count'] - 1)
                )
            )
    except KeyError:
        endpoint_map[logline[6]] = {"count": 1.0, "average": float(logline[9])}
    finally:
        maximum_up_to_now = reduce(max, (mapping['average'] for endpoint, mapping in endpoint_map.items()))
        for endpoint, mapping in endpoint_map.items():
            if mapping['average'] == maximum_up_to_now:
                endpoint_for_maximum = endpoint
        return endpoint_for_maximum, maximum_up_to_now


def get_maximum():
    endpoint_map = {}

    with open('access-log') as log:
        data_split = (line.split(' ') for line in log)
        data_structured = (calculate_max_until_now(logline=log, endpoint_map=endpoint_map) for log in data_split)
        return list(data_structured[-1])

def get_maximum_verb(verb):
    endpoint_map = {}
    with open('access-log') as log:
        data_split = (line.split(' ') for line in log)
        data_filtered = filterfalse(lambda: x:x[6] == f'"{verb}', data_split)
        data_structured = (calculate_max_until_now(logline=log, endpoint_map=endopint_map) for log in data_filtered)
        return list(data_structured[-1])


if __name__ == '__main__':
    maximum_all = get_maximum()
    maximum_post = get_maximum_verb('POST')
    maximum_get = get_maximum_verb('GET')
    print(f'\nMaximum of all: {maximum_all}\n\tMaximum POst: {maximum_post}\n\tMaximum Get: {maximum_get}')

