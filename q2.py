"""
Question 2.Create a function that takes an angle in radians and returns the corresponding angle
in degrees rounded to one decimal place.
Examples
radians_to_degrees(1) ➞ 57.3
radians_to_degrees(20) ➞ 1145.9
radians_to_degrees(50) ➞ 2864.8
"""

from math import pi

def radians_to_degrees(radian):
    degree = radian * 180 / pi
    return round(degree,1)

radians = int(input("Enter andle in radians and integer "))
degree = radians_to_degrees(radians)
print("radians_to_degrees(",radians ,") ➞ ", degree)