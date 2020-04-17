'''
Link : https://www.codechef.com/LRNDSA01/problems/FCTRL
'''

from sys import stdin,stdout

test=int(input())

while test:
    n=int(stdin.readline())
    
    count=0
    i=5
    while (n//i)>=1:
        count+=(n//i)
        i*=5

    
    stdout.write(str(count))
    stdout.write('\n')
    test-=1