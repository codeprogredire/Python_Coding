'''
Left-rotation in an array. Method-1(using temporary array)
Time complexity : O(d)
'''
print('Enter space-separated integers in the array : ')
nums=[int(i) for i in input().split()]
n=len(nums)
d=int(input('Enter the left-rotation unit : '))

print('Before : {}'.format(nums))

for i in range(d):
    temp=[nums[0]]
    nums=nums[1:]+temp

print('After : {}'.format(nums))
