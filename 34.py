'''
Calculate maximum sum of k-consecutive elements in array.
Window Sliding technique -- O(n)
'''


nums=list(map(int,input().split()))
k=int(input())

if k>len(nums):
    print('Invalid sub-array length')
else:
    window_sum=0

    for i in range(k):
        window_sum+=nums[i]

    max_sum=window_sum
    n=len(nums)
    for i in range(n-k):
        window_sum=window_sum-nums[i]+nums[i+k]
        max_sum=max(max_sum,window_sum)
        

    print(max_sum)