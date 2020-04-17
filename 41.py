'''
Link : https://www.codechef.com/LRNDSA01/problems/CONFLIP
'''

from sys import stdin,stdout

test=int(stdin.readline())

while test:
    G=int(stdin.readline())
    while G:
        I,N,Q=[int(i) for i in stdin.readline().split()]

        if N%2:
            if I==Q:
                stdout.write(str(N//2))
            else:
                stdout.write(str(N-(N//2)))
        else:
            stdout.write(str(N//2))
        stdout.write('\n')
        G-=1
    
    test-=1
        