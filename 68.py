from sys import stdin,stdout
from collections import defaultdict

N=int(stdin.readline())

hashmap=defaultdict()
visited=defaultdict()

for i in range(1,N+1):
    hashmap[i]=int(stdin.readline())
    visited[i]=False

total=0

for i,v in hashmap.items():
    if i==v:
        visited[i]=True
    length=0
    while visited[i]!=True:
        length+=1
        visited[i]=True
        i=hashmap[i]

    total+=max(0,length-1)

stdout.write(str(total))