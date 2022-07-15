"""
Question 3. In this challenge, establish if a given integer num is a Curzon number. If 1 plus
2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon
number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon
number, or False otherwise.
Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11
"""
import math

def its_curzon(num):
    while True:
        if num < 0 :
            num = int(input("Enter a n0n - negative number "))
            continue
        num1 = math.pow(2,num) + 1
        num2 = 2 * 5 + 1
        if num1 % num2 == 0:
            return True
        else:
            return False

num = int(input("Enter number to check "))
print("its_curzon(",num,") ➞ " , its_curzon(num))
