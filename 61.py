'''
Link : https://www.codechef.com/problems/SHUFFLE
'''

from sys import stdin,stdout
from collections import defaultdict,deque


for _ in range(int(stdin.readline())):
    n,k=list(map(int,stdin.readline().split()))
    nums=list(map(int,stdin.readline().split()))

    hashmap=defaultdict()

    for i in range(n):
        index=i%k
        if index in hashmap.keys():
            hashmap[index].append(nums[i])
        else:
            hashmap[index]=deque()
            hashmap[index].append(nums[i])

    for i,v in hashmap.items():
        hashmap[i%k]=deque(sorted(v))

    for i in range(n):
        nums[i]=hashmap[i%k].popleft()

    ans='yes\n'
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            ans='no\n'
            break

    stdout.write(ans)

        


    


