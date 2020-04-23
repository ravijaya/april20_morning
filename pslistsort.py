"""is there a way to sort based on ascii value for a list having mix of int, string"""


items = [2.2, 'pam', .98, 1, 'eva', 'tim', 'kimberly', 2, 10, 3,  111, 1.2, 'jane', 1000, 'jack']
items.sort(key=str)
print(items)
print()

items.sort(key=str, reverse=True)
print(items)
print()


# print(bin)
# print(bin(123))