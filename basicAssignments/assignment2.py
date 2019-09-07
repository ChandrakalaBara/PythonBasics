#  Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

radius = float(input('Enter the radius of the circle '))

area = math.pi * radius * radius

print('Area of the circle is %.16f' %area)

