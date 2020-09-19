# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:42:34 2020

@author: viswa
"""

def fib(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif(memo[n] != None):
        return memo[n]
    else:
        result = fib(n-1,memo) + fib(n-2, memo)
        memo[n] = result
        return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib(n, memo)

fib_memo(35)