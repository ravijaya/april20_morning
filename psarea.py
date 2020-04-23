"""demo  for the IO"""

# import math
from math import pi, sin, tan   # cherry picking


def compute(radius):
    """function definition"""
    return pi * radius ** 2


try:
    user_radius = float(input('enter the radius :'))
    area = compute(user_radius)  # function calling
    print('area :', area)
except ValueError as error:
    print(error)
