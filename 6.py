'''
Left-rotation in an array. Method-1(using temporary array)
Space complexity : O(n)
'''
print('Enter space-separated integers in the array : ')
nums=[int(i) for i in input().split()]
n=len(nums)
nums=nums+nums
d=int(input('Enter the left-rotation unit : '))

print(nums[d:d+n])