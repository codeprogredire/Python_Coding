'''
Link: https://www.spoj.com/problems/DQUERY/
'''


from sys import stdin,stdout
import math

def add(idx):
    global count
    freq[nums[idx]]+=1
    if freq[nums[idx]]==1:
        count+=1

def remove(idx):
    global count
    freq[nums[idx]]-=1
    if freq[nums[idx]]==0:
        count-=1

n=int(stdin.readline())
nums=list(map(int,stdin.readline().split()))

blk=200

q=int(stdin.readline())

queries=[]

freq=[0]*(n+1)

for i in range(q):
    query=list(map(int,stdin.readline().split()))
    query=tuple((query[0]-1,query[1]-1,i))
    queries.append(query)

print(queries)

queries.sort(key=lambda val:val[1])

ans=[0]*q

ml=0;mr=-1

for query in queries:
    L=query[0]
    R=query[1]
    
    count=0

    while mr<R:
        mr+=1
        add(mr)
    
    while ml>L:
        ml-=1
        add(ml)
    
    while mr>R:
        mr-=1
        remove(mr)

    while ml<L:
        ml+=1
        remove(ml)

    ans[query[2]]=count

print(ans)



