'''
Transpose and flatten matrix

Link : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
'''

import numpy as np

n,m=map(int,input().split())

a=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    a.append(temp)

a=np.array(a)
print(np.transpose(a))
print(a.flatten())
