items = (2.2, 'pam', 1.2, .98, 'andy', 'jane', 'neil', 'amanda', 2.3, 2)
print(items)
print(type(items))
print(len(items))
print()
# items[-1] = 'two'  # immutable object

print(items[-4])  # indexing
print(items[-4:])  # slicing
print()
    
for item in items[-4:]:   # iterate
    print(item)