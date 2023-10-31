import json
import csv
from collections import defaultdict
from pathlib import Path
from pprint import pprint
from io import StringIO

# class RegisterMeta(type):
#     def __new__(mcs, name, bases, namespace, **kwargs):
#         cls = super().__new__(mcs, name, bases, namespace)
#         cls.register(**kwargs)
#         return cls

class TableDecoder():
    _registry = {}

    @classmethod
    def __init_subclass__(cls, *, extension, **kwargs):
        super().__init_subclass__(**kwargs)
        if extension is None:
            return
        cls._registry[extension] = cls

    @classmethod
    def create(cls, name):
        decoder_class = cls._registry[name]
        return decoder_class()

    @classmethod
    def decoders(cls):
        return list(cls._registry.keys())

    def decode(self, text):
        raise NotImplementedError

class JsonTableDecoder(TableDecoder, extension ='json'):
    def decode(self, text):
        objs = json.loads(text)
        table = defaultdict(list)
        for obj in objs:
            for k, v in obj.items():
                table[k].append(v)
        return dict(table)

# JsonTableDecoder.register()
class CsvTableDecoder(TableDecoder, extension='csv'):
    def decode(self, text):
        with StringIO(text) as csv_stream:
            reader = csv.DictReader(csv_stream)
            table = defaultdict(list)
            for row in reader:
                for k, v in row.items():
                    table[k].append(int(v))
            return dict(table)

# CsvTableDecoder.register()
def load_table(filepath):
    filepath = Path(filepath)
    text = filepath.read_text()
    # decoder = JsonTableDecoder()
    # decoder = CsvTableDecoder()
    extension = filepath.suffix.lower().removeprefix('.')
    decoder = TableDecoder.create(extension)
    table = decoder.decode(text)
    return table


def main():
    # table = load_table('table.json')
    table = load_table('table.csv')
    pprint(table)


if __name__ == '__main__':
    pprint(TableDecoder.decoders())
    main()
