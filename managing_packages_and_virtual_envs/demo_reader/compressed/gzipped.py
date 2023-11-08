import gzip
#from demo_reader.util import writer
from ..util import writer
opener = gzip.open

if __name__ == '__main__':
    writer.main(opener)
