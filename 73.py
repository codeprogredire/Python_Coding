'''
Link: https://www.spoj.com/problems/AGGRCOW/
'''

from sys import stdin,stdout

def bs(arr):
    lo=0 # minimum distance possible
    hi=arr[-1]-arr[0] # maximum distance possible
    ans=0
    while lo<hi:
        mid=(lo+hi)//2
        if helper(arr,mid):
            ans=max(ans,mid)
            lo=mid+1
        else:
            hi=mid

    return ans


def helper(arr,dist):
    cows=1
    pos=arr[0]
    for i in range(1,n):
        if arr[i]-pos>=dist:
            pos=arr[i]
            cows+=1
        if cows==c:
            return True
    return False




for _ in range(int(stdin.readline())):
    n,c=list(map(int,stdin.readline().split()))
    locs=[0]*n
    for i in range(n):
        locs[i]=int(stdin.readline())
    
    locs.sort()
    
    stdout.write(str(bs(locs))+'\n')
    
