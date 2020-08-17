'''
Link: https://www.codechef.com/AUG20B/problems/CHEFWARS
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    h,p=list(map(int,stdin.readline().split()))

    if h==p:
        stdout.write('1\n')
    
    while h>0 and p>0:
        h=h-p
        p=p//2

    if h==p or p>0:
        stdout.write('1\n')
    else:
        stdout.write('0\n')
    