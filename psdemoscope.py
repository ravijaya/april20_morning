"""demo  for the scope"""

n = 100   # global scope


def demo():
    global n
    n = 'pip'   # update global variable from the function
    print(n)


print(n)
demo()
print(n)