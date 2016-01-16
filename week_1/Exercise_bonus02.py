'''
Program that displays the area and perimeter of a circle that has a radius of 5.5 using the
following formulas:
area = radius * radius * p
perimeter = 2 * radius * p
'''
from math import pi
radius = 5.5
print('{0:.2f}'.format(radius * radius * pi))
print('{0:.2f}'.format(2 * radius * pi))
