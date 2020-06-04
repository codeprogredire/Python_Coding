'''
1-D peak finding problem: Problem from 6006 MIT OCW Lecture 1
'''

def peakFind(arr):
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        if lo==hi:
            return arr[lo]
        if (hi-lo)==1:
            return max(arr[lo],arr[hi])
        
        mid=(lo+hi)//2
        
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return arr[mid]
        if arr[mid-1]>arr[mid]:
            hi=mid-1
        else:
            lo=mid+1

arr=list(map(int,input().split()))

print(peakFind(arr))