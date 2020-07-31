"""
You have two integer arrays, a and b, and an integer target value v. 
Determine whether there is a pair of numbers, where one number is taken from a and the other from b,
that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false
a = [1, 2, 3]
b = [10, 20, 30, 40]
v = 42
sumOfTwo(a, b, v) = True
"""

#Brute Force Solution

a = [1, 2, 3]
b = [10, 20, 30, 40]

def sumOfTwoBrute(a,b,v):
    for value in a:
        needed_value = v - value
        for values in b:
            if values == needed_value:
                return True
    return False

# print(sumOfTwoBrute(a,b, 44))

# O(n) time computation using sets or Hash set in python
def sumOfTwo(a, b, v):
    complement = set()
    for i in a:
        delta = i - v
        complement.add(delta)
    for j in b:
        if j == delta:
            return True
    return False

print(sumOfTwo(a, b, 412))