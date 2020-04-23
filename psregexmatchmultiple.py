"""match multiple times """

import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy match, atleast

for m in re.finditer(pattern, s, re.I):
    print(m)
    print(m.group())
    print(m.span())
    print()
