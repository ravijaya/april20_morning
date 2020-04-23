"""variable len arguments function"""


def demo(*args):
    """variable length arguments, yet another use case for tuple """
    print(args)


demo()
demo(123)
demo(1, 2, 'iii', 4, 5.5)
print()
demo('ravi')
demo(*'ravi')
# exit(1)
print()
items = [11, 22, 33]
demo(items)
demo(*items)   # to pass content of the object as the argument
print()

items = (11, 22, 33)
demo(items)
demo(*items)
print()
