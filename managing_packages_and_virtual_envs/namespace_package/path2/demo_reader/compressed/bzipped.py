import bz2
#from demo_reader.util import writer
#from ..util import writer
from .. import util

opener = bz2.open
if __name__ == '__main__':
    #writer.main(opener)
    util.writer.main(opener)
