import configparser
import re
import shlex

class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        return shlex.split(self.config['tox']['envlist'])
        """envs= re.split('\n|,',self.config['tox']['envlist'])
        return [item.strip() for item in envs if item.strip()]
        """

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        python_found = [self.config[section].get('basepython') for section in self.config.sections()]
        return list(set(item for item in python_found if item)) 
    

sample_ini_file = django = """# Tox (https://tox.readthedocs.io/) is a tool for running tests in multiple
# virtualenvs. This configuration file helps to run the test suite on all
# supported Python versions. To use it, "pip install tox" and then run "tox"
# from this directory.
#
# copied from: https://github.com/django/django/blob/master/tox.ini

[tox]
skipsdist = true
envlist =
    py3,
    flake8,
    docs,
    isort

# Add environment to use the default python3 installation
[testenv:py3]
basepython = python3

[testenv]
usedevelop = true
passenv = DJANGO_SETTINGS_MODULE PYTHONPATH HOME DISPLAY
setenv =
    PYTHONDONTWRITEBYTECODE=1
deps =
    py{3,35,36,37}: -rtests/requirements/py3.txt
    postgres: -rtests/requirements/postgres.txt
    mysql: -rtests/requirements/mysql.txt
    oracle: -rtests/requirements/oracle.txt
changedir = tests
commands =
    {envpython} runtests.py {posargs}

[testenv:flake8]
basepython = python3
usedevelop = false
deps = flake8
changedir = {toxinidir}
commands = flake8 .

[testenv:docs]
basepython = python3
usedevelop = false
whitelist_externals =
    make
deps =
    Sphinx
    pyenchant
    sphinxcontrib-spelling
changedir = docs
commands =
    make spelling

[testenv:isort]
basepython = python3
usedevelop = false
deps = isort
changedir = {toxinidir}
commands = isort --recursive --check-only --diff django tests scripts

[testenv:javascript]
usedevelop = false
deps =
changedir = {toxinidir}
whitelist_externals = npm
commands =
    npm install
    npm test"""
    
    
filename = "/tmp/test_file.ini"
with open(filename,'w') as f:
    f.write(sample_ini_file)



tox = ToxIniParser(filename)
print(tox.number_of_sections)
print(tox.environments)
print(tox.base_python_versions)
