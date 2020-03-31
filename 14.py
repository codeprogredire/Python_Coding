'''
Concatenate arrays
Link : https://www.hackerrank.com/challenges/np-concatenate/problem
'''

import numpy as np

n,m,p=[int(i) for i in input().split()]

a=[]
for _ in range(n):
    temp=[int(i) for i in input().split()]
    a.append(temp)

b=[]
for _ in range(m):
    temp=[int(i) for i in input().split()]
    b.append(temp)

a=np.array(a)
b=np.array(b)

print(np.concatenate((a,b),axxis=0))
