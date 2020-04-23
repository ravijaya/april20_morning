"""demo for the integer"""

n = 15
print(n)
print(type(n))
print()

print(0xf)  # different int
print(0o17)
print(0b1111)
print()

print(hex(n))
print(oct(n))
print(bin(n))  # base 10 to other number system
print()

# convert other number system into base 10
print(int('f', 16))
print(int('17', 8))
print(int('1111', 2))
print()

print(8 / 3)
