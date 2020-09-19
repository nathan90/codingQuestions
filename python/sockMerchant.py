# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:16:10 2020

@author: viswa
"""
#https://www.hackerrank.com/challenges/sock-merchant/problem

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    x = set()
    pairs = 0
    for a in ar:
        if a not in x:
            x.add(a)
        elif a in x:
            pairs += 1
            x.remove(a)
    print(x)
    print(pairs)
        
sockMerchant(n,ar)