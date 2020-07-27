'''
Link: https://www.spoj.com/problems/RMQSQ/
'''

from sys import stdin,stdout
import math

n=int(stdin.readline())
nums=list(map(int,stdin.readline().split()))

bs=math.floor(math.sqrt(n))
n_blocks=math.ceil(n/bs)

blocks=[0]*n_blocks

i=0;k=0
while i<n:
    j=0;mn=float('inf')
    while j<bs and i<n:
        if nums[i]<mn:
            mn=nums[i]
        i+=1
        j+=1
    blocks[k]=mn
    k+=1


q=int(stdin.readline())

for _ in range(q):
    L,R=list(map(int,stdin.readline().split()))
    lb=L//bs
    rb=R//bs

    mn=float('inf')

    if lb==rb:
        for i in range(L,R+1):
            mn=min(nums[i],mn)
    else:
        for i in range(L,(lb+1)*bs):
            mn=min(nums[i],mn)
        
        for i in range(lb+1,rb):
            mn=min(blocks[i],mn)
        
        for i in range(rb*bs,R+1):
            mn=min(nums[i],mn)

    stdout.write(str(mn)+'\n')


