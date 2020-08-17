'''
Link: https://www.spoj.com/problems/DQUERY/
'''

from sys import stdin,stdout
import math

class Query:
    def __init__(self,idx,l,r):
        self.idx=idx
        self.L=l
        self.R=r


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

q=int(stdin.readline())

queries=[]

freq=[0]*pow(10,6)

for i in range(q):
    l,r=list(map(int,stdin.readline().split()))
    l,r=l-1,r-1
    query=Query(i,l,r)
    queries.append(query)

queries.sort(key=lambda x: x.R)

ans=[0]*q

ml=0;mr=-1

count=0

for query in queries:
    L=query.L
    R=query.R
    
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
        remove(ml)
        ml+=1

    ans[query.idx]=count

for i in ans:
    stdout.write(str(i)+'\n')