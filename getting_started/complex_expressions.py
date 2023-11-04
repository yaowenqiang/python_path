import os
from icecream import ic
import glob
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
ic(file_sizes)
