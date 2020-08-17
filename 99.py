'''
Sqrt decomposition

Given an array of n elements. We need to answer q 
queries telling the sum of elements in range l to 
r in the array.
'''


from sys import stdin,stdout
import math

# if dynamic array
def update(val,idx):
    blk_idx=idx//blk_size
    blk[blk_idx]-=arr[idx]
    blk[blk_idx]+=val
    arr[idx]=val

n=int(stdin.readline())

arr=list(map(int,stdin.readline().split()))

blk_size=math.ceil(math.sqrt(n))

n_blocks=math.ceil(n/blk_size)


blk=[0]*blk_size
blk_idx=-1
for i in range(n):
    if i%blk_size==0:
        blk_idx+=1
    blk[blk_idx]+=arr[i]

print(blk)

q=int(stdin.readline())

for _ in range(q):
    query=list(map(int,stdin.readline().split()))
    l=query[0]
    r=query[1]

    lb=l//blk_size
    rb=r//blk_size

    ans=0
    if lb==rb:
        for i in range(l,r+1):
            ans+=arr[i]
            print(ans)
    else:
        for i in range(l,(lb+1)*blk_size):
            ans+=arr[i]
        print(ans)
        
        for i in range(lb+1,rb):
            ans+=blk[i]
        print(ans)        

        for i in range(rb*blk_size,r+1):
            ans+=arr[i]
        print(ans)        

    stdout.write(str(ans)+'\n')

        

