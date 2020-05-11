from sys import stdin,stdout
import numpy as np



for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nums = list(map(int,stdin.readline().split()))

    for i in range(n):
        if abs(nums[i])%4==0:
            nums[i]=2
        elif abs(nums[i])%2==0:
            nums[i]=1
        else:
            nums[i]=0

    print(nums)




