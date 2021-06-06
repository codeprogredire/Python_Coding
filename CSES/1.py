'''
Link: https://cses.fi/problemset/task/1068
'''

from sys import stdin,stdout

n = int(stdin.readline())

if n>=1:
    stdout.write(str(n)+' ')

    while n!=1:
        if n%2==0:
            n//=2
        else:
            n=3*n+1
        stdout.write(str(n)+' ')