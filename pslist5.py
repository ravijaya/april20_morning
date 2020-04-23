tiny = [2.2, 0.98, 2, 3, 1.2]

print(tiny + tiny)
print()
print(tiny * 3)
print()

duplicates = [2.2, 0.98, 2, 3, 1.2, 2.2, 0.98, 2, 3, 1.2, 2.2, 0.98, 2, 3, 1.2]
duplicates.sort() # inplace edit
print(duplicates)
print()

duplicates = [2.2, 0.98, 2, 3, 1.2, 2.2, 0.98, 2, 3, 1.2, 2.2, 0.98, 2, 3, 1.2]
duplicates.sort(reverse=True) # inplace edit
print(duplicates)
print()


"""is there a way to sort based on ascii value for a list having mix of int, string"""

