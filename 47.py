from sys import stdin,stdout
from collections import deque

test=int(stdin.readline())

for _ in range(test):
    n,m,c=stdin.readline().split()

    n=bin(int(n))[2:]
    n='0'*(16-len(n))+n
    d=deque(n)
    if c=='L':
        d.rotate(-int(m))
    else:
        d.rotate(int(m))
    
    ans=''.join(d)
    stdout.write(str(int(ans,2))+'\n')

