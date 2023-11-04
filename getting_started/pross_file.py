# process file ,LBYL

import os


p = 'path/to/datafile.dat'

if os.path.exists(p):
    process_file(p)
else:
    print(f'No such file as {p}')

# process file ,EAFP

import os


p = 'path/to/datafile.dat'

try:
    process_file(p)
except OSError as e:
    print(f'Error: {e}')
