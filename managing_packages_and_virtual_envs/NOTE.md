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
