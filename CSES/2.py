'''
Link: https://cses.fi/problemset/task/1083
'''

from sys import stdin,stdout

n = int(stdin.readline())

nums = [int(i) for i in stdin.readline().split()]

sum = 0

for num in nums:
    sum+=num

tot = n*(n+1)//2

stdout.write(str(tot-sum))