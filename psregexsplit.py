import re

s = 'root:x,0 0;root:/root,/bin/bash'
pattern = '[:, ;]'

items = re.split(pattern, s)     # regex split
print(items)
