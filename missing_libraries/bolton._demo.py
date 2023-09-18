# https://boltons.readthedocs.io/en/latest/

from boltons import jsonutils, timeutils, iterutils
from datetime import date
from pprint import pprint

with open('input.jsonl') as f:
    for line in jsonutils.JSONLIterator(f):
        print(f"User: {line['name']} with ID {line['id']} is {'active' if line['active'] else 'inactive'}")

start_date = date(year=2023, month=4, day=9)
end_date = date(year=2023, month=4, day=30)
for day in timeutils.daterange(start_date, end_date, step=(0,0,2)):
    print(repr(day))

data = {"deeply": {"nested": {"python":{"dict":"value"}}}}
path = iterutils.get_path(data, ('deeply', 'nested', 'python'))
pprint(path)

data = {"id":"234411",
        "node1":{"id":1234, "value": "some data"},
        "node2":{"id":2352345,
                 "node3":{"id":"123422", "value":"more data"}
                }
       }
new_data = iterutils.remap(data, lambda p, k, v : (k, int(v)) if k == 'id' else (k,v))
pprint(new_data)
