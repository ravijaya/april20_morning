from csv import reader
from pprint import pprint  as pp
from json import dump


# json

keys = ['password', 'uid', 'gid', 'gecos', 'home', 'shell']
# values = ['x', '0', '0', 'root', '/root', '/bin/bash']
#
# print(zip(keys, values))
# print(dict(zip(keys, values)))

container = {}

for row in reader(open('passwd.txt'), delimiter=':'):
    login, user_info = row[0], row[1:]
    container[login] = dict(zip(keys, user_info))

pp(container)
dump(container, open('passwd.json', 'w'), indent=2)

# serialize into json
