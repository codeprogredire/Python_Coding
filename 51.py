import itertools
from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n,r,k=[int(i) for i in stdin.readline().split()]

    nums=list(range(1,n+1))

    nums=list(itertools.permutations(nums))

    ans=[]
    for arr in nums:
        count=0
        arr=list(arr)
        size=len(arr)
        for i in range(size):
            for j in range(i+1,size):
                if arr[i]>arr[j]:
                    count+=1

        if count==r:
            ans.append(arr)
    for i in ans[k-1]:
        stdout.write(str(i)+' ')
    stdout.write('\n')

