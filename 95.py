'''
Link: https://www.codechef.com/problems/CHECHOC
'''

from sys import stdin,stdout
import math

for _ in range(int(stdin.readline())):
    n,m,x,y=list(map(int,stdin.readline().split()))

    size=n*m
    if size==1:
        ans=x
    elif x>y:
        ans=math.ceil(size/2)*y
    elif 2*x<y:
        ans=size*x
    elif size%2==0:
        ans=(size//2)*y
    else:
        ans=(size//2)*y+x
    
    stdout.write(str(ans)+'\n')
