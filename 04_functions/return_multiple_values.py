# Create a function that returns both the area and circumference of a circle given its radius
# Area of circle: (pi * radius)square A
# Circumference: 2 * pi * radius

pi = 3.14  # we can also import math library for getting pi value using math.pi()
def area_and_circumference(radius):
    area = pi * (radius**radius)
    circumference = 2 * pi * radius
    return area, circumference

a, c = area_and_circumference(2)

print("Area:",a,"Circumference:",c)