from sys import stdin,stdout
import math
from collections import Counter

n=int(stdin.readline())

arr=[]

for _ in range(n):
    temp=stdin.readline().rstrip()
    arr.append(temp)

n_blk=math.ceil(math.sqrt(n))
blk_size=math.ceil(n/n_blk)

blk=[]

k=0
for i in range(n_blk):
    temp=[]
    j=0
    while j<blk_size and k<n:
        temp.append(arr[k])
        j+=1
        k+=1
    
    counter=dict(Counter(temp))
    blk.append(counter)

q=int(stdin.readline())

for i in range(int(q)):
    query=list(stdin.readline().split())
    l=int(query[0])-1
    r=int(query[1])-1
    s=query[2]

    L=l//blk_size
    R=r//blk_size

    if L==R:
        count=0
        for i in range(l,r+1):
            if arr[i]==s:
                count+=1

        ans=count
    else:
        count=0
        for i in range(l,(L+1)*blk_size):
            if arr[i]==s:
                count+=1
        
        temp=0
        for i in range((L+1),R):
            if s in blk[i]:
                temp+=blk[i]
        count+=temp

        for i in range(R*blk_size,r+1):
            if arr[i]==s:
                count+=1
        
        ans=count
    
    stdout.write(str(ans)+'\n')

