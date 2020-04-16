'''
Move zeros : Leetcode
Link : https://leetcode.com/problems/move-zeroes/
'''

nums = list(map(int,input().split()))

count = 0
i=0
n=len(nums)
while i<n:
    if nums[i]==0:
        count+=1
        del(nums[i])
        n-=1
    else:
        i+=1

nums+=[0]*count

print(nums)
