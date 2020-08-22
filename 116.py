'''
Link: https://www.interviewbit.com/problems/partitions/
'''

def find(nums,target):
    hi=len(nums)-1
    lo=0

    while lo<hi:
        mid=(lo+hi)//2
        if nums[mid]>target:
            hi=mid
        else:
            lo=mid+1
    
    return hi
        
def solve(nums,n):
    tot=sum(nums)
    if tot%3!=0:
        return 0
    else:
        part=tot//3
        left=[]
        right=[]
        
        leftSum=0
        rightSum=0
        
        for i,v in enumerate(nums):
            leftSum+=v
            idx=n-1-i
            rightSum+=(nums[idx])
            if leftSum==part:
                left.append(i)
            if rightSum==part:
                right=[idx-1]+right

        count=0

        for target in left:
            idx=find(right,target)

            if idx==len(right)-1 and right[idx]<=target:
                count+=0
            else:
                count+=(len(right)-idx)
                
        return count
            
nums=list(map(int,input().split()))
n=int(input())
print(solve(nums,n))