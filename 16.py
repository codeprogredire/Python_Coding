'''
Array Mathematics
Link : https://www.hackerrank.com/challenges/np-array-mathematics/problem
'''
import numpy as np

n,m=list(map(int,input().split()))

a=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    a.append(temp)

b=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    b.append(temp)

a=np.array(a)
b=np.array(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)



