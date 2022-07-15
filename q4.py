"""
Question 4.Given the side length x find the area of a hexagon.
Examples
area_of_hexagon(1) ➞ 2.6
area_of_hexagon(2) ➞ 10.4
area_of_hexagon(3) ➞ 23.4
"""
import math

def area(s):
    c = math.sqrt(3) * 3 / 2
    return round(c*s*s,1)

s = float(input("Enter side "))
print("area_of_hexagon(",s,") ➞ ",area(s))