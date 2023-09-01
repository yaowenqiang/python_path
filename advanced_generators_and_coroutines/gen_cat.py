from pathlib import Path
import gzip, bz2

def gen_open(paths):
    for path in paths:
        if path.suffix == '.gz':
            yield gzip.open(path, 'rt')
        elif path.suffix == '.bz2':
            yield bz2.open(path, 'rt')
        else:
            yield open(path, 'rt')
def gen_cat(sources):
    for scr in sources:
        for item in src:
            yield item

def gen_cat2(sources):
    for scr in sources:
        yield from src

lognames = Path('/usr/www/').rglob('access-log')
logfiles = gen_open(lognames)
loglines = gen_cat(logfiles)
