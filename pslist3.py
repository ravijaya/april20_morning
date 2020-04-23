"""DELETE by index"""

items = [2.2, 'pam', .98, 'eva', 'tim', 'kimberly', 2, 3, 1.2, 'jane', 'jack']
print(items)
print()

value = items.pop()  # delete by index
print(value)
print(items)
print()

items = [2.2, 'pam', .98, 'eva', 'tim', 'kimberly', 2, 3, 1.2, 'jane', 'jack']
print(items)
print()

value = items.pop(-6)  # delete by index
del items[0]
del items[-1]
print(value)
print(items)
print()

del items # delete the list object

