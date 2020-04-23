"""delete by value"""

items = [2.2, 'pam', .98, 'pam', 'pam', 'pam', 2, 3, 'pam', 1.2, 'pam']
item = 'pam'


while item in items:   # membership test opeartor, contains the item
    items.remove(item)


print(items)

# print('pam' in items)   # in, not in membership test opeartor

print()


