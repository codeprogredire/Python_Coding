from sys import stdin,stdout
import itertools

for _ in range(int(stdin.readline())):
    K,Q=list(map(int,stdin.readline().split()))
    m=list(map(int,stdin.readline().split()))
    s=list(map(int,stdin.readline().split()))
    m.sort()
    s.sort()
    temp=itertools.product(m,s)
    nums=[0]*(K**2)
    for i,v in enumerate(temp):
        nums[i]=sum(v)

    nums.sort()

    for _ in range(Q):
        index=int(stdin.readline())
        stdout.write(str(nums[index-1])+'\n')



