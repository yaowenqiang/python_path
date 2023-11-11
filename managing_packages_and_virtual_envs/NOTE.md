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

python multi-reader-program # this will add multi-reader-program to sys.path
python multi-reader-program test.bz2

Executable Zip files
> python -m zipfile -c ../multi-reader.-program.zip *
> cd ..
> python multi-reader-program.zip test.bz2

Executable Packages

Executing Directories vs Packages

python directory  | python -m directory
----------------- | --------------------
Execute a directory  | Executing a package
'directory' added to sys.path  | - The '-m' tells Python to treat it as a module
'directory/__main__.py' is not in a package  | 'directory/__main__' is a submodule of the directory package

> python -m demo_reader test.gz


# Recommended Project Layout

# module plugins

implementing  Plugins with setuptools Entry Point

# Package Distribution

## Distribution Package

+ Archive of package contents
+ easy to install
+ Various formats
  + Zip files
  + tarballs
  + Wheels


Built vs Source Packages

+ Built
  + Placed directly into installation directory
  + Build results are included in the package
  + Can be platform-specific
+ Source
  + contains everything needed to build the package
  + Cannot be placed directly into installation directory
  + It is necessary to build the package before installing it



> python setup.py sdist
> pip install demo_reader-1.0.0.tar.gz

Use the Wheel format defined in PEP 427

> pip install wheel

> python setup.py bdist_whell

> pip install dist/demo-reader-1.0.0-py3-non-any.whl

+ py3  python version
+ none  API requirements(Application Binary Interface)
+ any Platform requirements

## Uploading Packages to a package Server

> pypi.org

register a account

> python -m pip  install --user --upgrade twine
> twine upload dist/demo-reader-1.0.0-py3-non-any.whl
>
> pip install demo_reader


