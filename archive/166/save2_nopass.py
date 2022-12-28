import configparser


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
        return self.config['tox']['envlist']

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        return [self.config[section].get('basepython') for section in self.config.sections()]
            
    

sample_ini_file = """[tox]
envlist = py27, py34, py35, py36, pypy, flake8

[testenv]
passenv = LC_ALL, LANG, HOME
commands = pytest --cov=cookiecutter {posargs:tests}
deps = -rtest_requirements.txt

[testenv:flake8]
deps =
    flake8==3.5.0
commands =
    flake8 cookiecutter tests setup.py

[testenv:cov-report]
commands = pytest --cov=cookiecutter --cov-report=term --cov-report=html"""

filename = "/tmp/test_file.ini"
with open(filename,'w') as f:
    f.write(sample_ini_file)


#config = configparser.ConfigParser()
#config.read(filename)
#print(config.sections())
tox = ToxIniParser(filename)
print(tox.number_of_sections)
print(tox.environments)
print(tox.base_python_versions)
