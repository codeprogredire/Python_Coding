from sys import stdin,stdout

test=int(stdin.readline())

for _ in range(test):
    n,k=[int(i) for i in stdin.readline().split()]
    nums=[int(i) for i in stdin.readline().split()]

    for i in range(n-k):
        if nums[i]>=nums[i+k]:
            nums[i],nums[i+k]=nums[i+k],nums[i]


    ans='yes'
    
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            ans='no'
            break
    
    stdout.write(ans)
    stdout.write('\n')
    





    