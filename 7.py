'''
Left-rotation in an array. Method-1(using temporary array)
Space complexity : O(d), number of left-displacement unit
'''
print('Enter space-separated integers in the array : ')
nums=[int(i) for i in input().split()]
n=len(nums)
d=int(input('Enter the left-rotation unit : '))
temp=nums[:d]
print(nums[d:]+temp)