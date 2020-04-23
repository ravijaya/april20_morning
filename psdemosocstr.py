"""multi-line formatted content"""

s = """
   {}
  2 2
 3 {} 3
  4 4
   {}   
"""
alpha, beta, charlie = 'x', 'y', 'z'
print(s.format(alpha, beta, charlie))  # string formatting
print()

name, age = 'sarah', 3  # unpacking aka parallel assignment
content = 'i am name, age years old'
print(content)
print()

content = f'i am {name}, {age} years old'  # formatted string
print(content)
print()
#
content = f'i am {name.title()}, {age * 3} years old'  # formatted string
print(content)
print()
