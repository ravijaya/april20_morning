"""application of set """

numbers = [1, 2, 3, 4, 5]
odds = [1, 3, 5, 7, 9]


a = set(numbers)
b = set(odds)

print(a.intersection(b))
print(a & b)
print()
print(a.union(b))
print(a | b)
print()
print(a.difference(b))
print(b - a)

