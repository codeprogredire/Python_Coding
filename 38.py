'''
Fast I/O
Link : https://www.spoj.com/problems/INTEST/
'''

from sys import stdin,stdout

n,k = [int(i) for i in stdin.readline().split()]

count=0

for i in range(n):
        num=int(stdin.readline())
        if num%k==0:
                count+=1

stdout.write(str(count))
