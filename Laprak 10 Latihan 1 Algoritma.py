# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:34:46 2022

@author: acer
"""

def tukar(a,i,j):
 t = a[i]
 a[i] = a[j]
 a[j] = t
def bubble_sort(a,n):
 for i in range (n-1):
     if a[i] > a[i+1]:
         tukar(a,i,i+1)
 if n - 1 > 1:
     bubble_sort(a,n-1)
a = [8,22,-6,1,12,30]
bubble_sort(a, len(a))
print("List yang sudah disorting")
print(a)