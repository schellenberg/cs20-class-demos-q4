# Area of a Circle Calculator
# Dan Schellenberg
# May 16, 2022

import math

# take user input
radius = input("Please enter the radius of the circle: ")

# convert to numbers
radius = int(radius)

# do the math
area = math.pi * radius ** 2

# print the result
print("The area is " + str(area))