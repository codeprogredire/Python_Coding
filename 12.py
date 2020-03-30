'''
(Climbing stairs problem)--Leetcode

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

import math

calculate = lambda n1,n2: math.factorial(n1+n2)/(math.factorial(n1)*math.factorial(n2))

n = int(input())

if n%2==0:
    min_steps = n//2
    n2=min_steps
    n1=0
else:
    min_steps=n//2 + 1
    n2=n//2
    n1=1
count=calculate(n1,n2)
min_steps+=1
while min_steps<=n:
    n2-=1
    n1+=2
    count+=calculate(n1,n2)
    min_steps+=1

print(int(count))
