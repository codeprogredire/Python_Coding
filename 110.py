'''
Link: https://www.codechef.com/DEM2020/problems/TOWIN
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    nums=list(map(int,stdin.readline().split()))
    if n==1:
        stdout.write(str('first\n'))
    elif n==2:
        if nums[0]==nums[1]:
            stdout.write(str('draw\n'))
        else:
            stdout.write('first\n')
    else:
        nums.sort(reverse=True)
        first=nums[0]
        sec=nums[1]+nums[2]

        if n==3:
            if sec>first:
                stdout.write('second\n')
            elif sec<first:
                stdout.write('first\n')
            else:
                stdout.write('draw\n')
        else:
            for i in range(3,n,2):
                first+=nums[i]

            for i in range(4,n,2):
                sec+=nums[i]
            
            if sec>first:
                stdout.write('second\n')
            elif sec<first:
                stdout.write('first\n')
            else:
                stdout.write('draw\n')

            
        



    