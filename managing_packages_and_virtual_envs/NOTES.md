> pip -V
> apt-get install python3-pip

> pip list -o 


> pip install six Django Keras

# Virtual env

> python -m pip install virtualenv

> which virtualenv

> python -m pip uninstall virtualenv

> sudo python -m pip install virtualenv

> virtualenv envname

> virtualenv -p python3 envname

> python -m venv envname


> pyvenv envname


> pip install box

> python -m pip  freeze

> python -m pip  freeze > requirements.txt


## Specify Versions

docopt == 0.6.5 # must be version 0.6.5
keyring >=4.1.1 # Minimum version 4.1.1
coverage != 3.5 # Anything except version 3.5

python -m pip install flask=0.9

python -m pip install 'Django<2.0' # Mind the quotes!

> python -m pip install -U flask

> python -m pip install -U pip

> python -m pip install -e flask # install from local disk

## tox

> python -m pip install tox

> tox

## Virtualenvwrapper

> virtualenvwrapper-win

> sudo pip install virtualenvwrapper

> which virtualenvwrapper.sh

> vim .profile

> source Virtualenvwrapper.sh_path
> export WORKON_HOME='/hoem/username/virtualenvs'

> workon

> workon projectname

> deactivate



> mkproject new_proj


> mkproject -p python3 new_proj

> setvirtualenvproject

> mkvirtualenv new_env

> rmvirtualenv new_env

> mktmpenv

> export WORKON_HOME=''
> export PROJECT_HOME='' # Needed for mkproject


##  modern tools

> https://pypa.io

Installation

+ pip
  + wheels
  + eggs
+ easy_install
  + don't use

Dependency management

+ requirements.txt

Project isolation

+ virtualenv
+ venv


new projects


+ pipenv
+ poetry
+ Anaconda


Requirements 

requirements.txt

+ Standard(pip)
+ Not deterministic

Pipfile

+ pipenv
+ Custom format
+ Deterministic


pyproject.toml

+ poetry
+ Standard(PEP-518)
+ Deterministic

## pipenv

> sudo pip install pipenv

> pipenv install requests python-box

> pipenv run python script.py

> pipenv shell

> exit

> pipenv install --three


### poetry

> poetry new envname
> poetry add requests python-box

> poetry run python scriptname

> poetry shell




























