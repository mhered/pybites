import random
from pprint import pprint 

names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*argv):
    return (SEPARATOR.join([str(arg[i]) for arg in argv]) for i in range(0,len(argv[0])))
        

pprint(list(generate_table(names, aliases,points,awake)))