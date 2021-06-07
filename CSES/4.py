'''
Link: https://cses.fi/problemset/task/1094
'''

from sys import stdin, stdout

n = int(stdin.readline())
nums = [int(i) for i in stdin.readline().split()]

moves = 0

for i in range(1,n):
    if nums[i]<nums[i-1]:
        moves+=(nums[i-1]-nums[i])
        nums[i]=nums[i-1]

stdout.write(str(moves))