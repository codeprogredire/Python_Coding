'''
Link: https://www.codechef.com/COLE2020/problems/CLPNT
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    nums=list(map(int,stdin.readline().split()))
    q=int(stdin.readline())
    for _ in range(q):
        x,y=list(map(int,stdin.readline().split()))
        ans=-1
        target=x+y

        lo=0;hi=n-1;

        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                ans=-2
                break
            elif nums[mid]<target:
                ans=mid
                lo=mid+1
            else:
                hi=mid-1

        stdout.write(str(ans+1)+'\n')