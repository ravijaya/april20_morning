from json import load
from pprint import pprint as pp

content = load(open('passwd.json'))  # read from the json into py

print(type(content))
pp(content)

# json 2 xlsx

# pypi
