"""
Question 5. Create a function that returns a base-2 (binary) representation of a base-10
(decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to
the left will be x2 the value, value of an 8 bit binary numbers are
 (256, 128, 64, 32, 16, 8, 4, 2, 1).
Examples
binary(1) ➞ "1"
# 1*1 = 1
binary(5) ➞ "101"
# 1*1 + 1*4 = 5
"""

def binary(n):
    l = []
    if n == 0:
        l.append(0)
    while n > 0:
        l.append(n % 2)
        n = int(n/2)
    l = reversed(l)
    s = ''
    for i in l:
        s = s + str(i)
    return s

n = int(input("Enter Decimal number "))
print("binary(" ,n,") ➞ " ,binary(n))