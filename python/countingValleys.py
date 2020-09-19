# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:50:22 2020

@author: viswa
"""
#https://www.hackerrank.com/challenges/counting-valleys

# n = 8
# s = "UDDDUDUU"

n = 12
s = "DDUUDDUDUUUD"

# Complete the countingValleys function below.
def countingValleys(n, s):
    no_of_valley = 0
    a = 0
    for i in s:
        if i == 'U':
            a += 1
        else:
            a -= 1
            if a == -1:
                no_of_valley +=1
        print (a)
    return no_of_valley


countingValleys(n,s)