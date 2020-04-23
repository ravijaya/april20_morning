"""demo for the bytes"""

s = b'python'
print(s)
print(type(s))
print(len(s))
print(s + s)
print(s.upper())
print()

print(s.decode())  # convert bytes into str (unicode)
print()

s = 'python'
print(s.encode())  # convert str into bytes
