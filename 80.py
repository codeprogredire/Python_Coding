'''
Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the 
numbers in the original array except the one at i.
(Asked by Uber)
'''

import math

arr=list(map(int,input().split()))

product=0

for i in arr:
    product+=math.log10(i)

ans=[0]*len(arr)

for i in range(len(arr)):
    ans[i]=math.ceil(pow(10.0,product-math.log10(arr[i])))

print(ans)
