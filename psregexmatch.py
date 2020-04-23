import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy match, atleast


m = re.search(pattern, s, re.I)

if m:
    print(m)
    print(type(m))
    print('match string :', m.group())
    print(m.start())
    print(m.end())
else:
    print('failed to match')
