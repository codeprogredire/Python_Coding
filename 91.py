from sys import stdin,stdout

n=int(stdin.readline())
nums=list(map(int,stdin.readline().split()))

nums.sort(reverse=True)

if n==3:
    if nums[1]+nums[2]>nums[0]:
        stdout.write('YES\n')
        stdout.write(str(nums[0])+' '+str(nums[1])+' '+str(nums[2]))

    else:
        stdout.write('NO')
else:
    if nums[1]+nums[2]>nums[0]:
        stdout.write('YES\n')
        stdout.write(str(nums[0])+' '+str(nums[1])+' '+str(nums[2]))
    else:
        ans='NO'
        for i in range(3,n):
            if nums[i]+nums[i-1]>nums[i-2]:
                ans='YES\n'
                stdout.write(ans)
                stdout.write(str(nums[i-2])+' '+str(nums[i-1])+' '+str(nums[i]))
                break

        if ans=='NO':
            stdout.write(ans)

            

