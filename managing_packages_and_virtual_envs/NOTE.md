on windows

> set PYTHONPATH=path1;path2;path3;


Linux/MacOS

> export PYTHONPATH=path1:path2:path3 

> https://docs.python.org/3/library/sys.html#sys.path
> https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH


PEP 420 and __init__.py

__init__.py is optional since Python 3.3+

> import demo_reader
> demo_reader.__file__


relative imports syntax 
from ..module_name import name

Relative imports from demo_reader/compressed/bzipped.py

relative | Absolute
-------- | -------- |
from . import name  |  from demo_reader.compressed import name
from .. import name  |  from demo_reader import name
from ..util import name  |  from demo_reader.util import name

PEP 420: Implicit Namespace Packages

Namespace package may not have __init__.py

Executable Directories

__main__.py

Executable Zip files
> python -m zipfile -c ../multi-reader.-program.zip *
> cd ..
> python multi-reader-program.zip test.bz2

Executable Packages

