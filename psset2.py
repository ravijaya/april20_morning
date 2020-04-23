items = {2.2, 'pam', 1.2, .98, 'andy', 'jane', 'neil', 'amanda', 2.3, 2 }  # immutable object
print(items)
print(len(items))
print()

items.add('tommy')
items.add(12.3212)
items.add('larry')
print(items)
print()

items.remove(.98)
items.remove('neil')
items.remove('pam')
print(items)
print()

# iterate
for item in items:
    print(item)