# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:32:32 2022

@author: acer
"""

def tukar(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubbleSort(A, n):
    for i in range(n-1):
        if A[i] > A[i + 1]:
            tukar(A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)

A = []
bubbleSort(A, len(A))
print("")
print(A)