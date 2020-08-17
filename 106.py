'''
Link: https://www.codechef.com/AUG20B/problems/LINCHESS
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n,k=list(map(int,stdin.readline().split()))
    pos=list(map(int,stdin.readline().split()))

    moves=float('inf')
    idx=-1

    for i,p in enumerate(pos):
        if k%p==0:
            temp=min((k//p-1)*p,moves)
            if temp!=moves:
                idx=i
            moves=temp

            
    
    if idx==-1:
        stdout.write(str('-1\n'))
    else:
        stdout.write(str(pos[idx])+'\n')

        

