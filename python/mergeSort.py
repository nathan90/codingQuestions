# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:04:59 2020

@author: viswa
"""
def merge_sort(array):
    if len(array) > 1:
        m = len(array)//2
        left = array[:m]
        right = array[m:]
        print(left, '<=left right=>', right)
        left = merge_sort(left)
        right = merge_sort(right)
        
        array = []
        
        while len(left) > 0 and len(right) > 0:
            if left[0]< right[0]:
                array.append(left[0])
                left.pop(0)
            else:
                array.append(right[0])
                right.pop(0)
        
        for i in left:
            array.append(i)
        for i in right:
            array.append(i)
    return array


merge_sort([4,3,2])