import json
import csv
from collections import defaultdict
from pathlib import Path
from pprint import pprint
from io import StringIO

class TableDecoder:
    def decode(self, text):
        raise NotImplementedError

class JsonTableDecoder(TableDecoder):
    def decode(self, text):
        objs = json.loads(text)
        table = defaultdict(list)
        for obj in objs:
            for k, v in obj.items():
                table[k].append(v)
        return dict(table)

class CsvTableDecoder(TableDecoder):
    def decode(self, text):
        with StringIO(text) as csv_stream:
            reader = csv.DictReader(csv_stream)
            table = defaultdict(list)
            for row in reader:
                for k, v in row.items():
                    table[k].append(int(v))
            return dict(table)

def load_table(filepath):
    filepath = Path(filepath)
    text = filepath.read_text()
    # decoder = JsonTableDecoder()
    decoder = CsvTableDecoder()
    table = decoder.decode(text)
    return table


def main():
    # table = load_table('table.json')
    table = load_table('table.csv')
    pprint(table)


if __name__ == '__main__':
    main()
