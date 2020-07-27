'''
Link: https://www.codechef.com/COOK120B/problems/XORCIST
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    N,Q=list(map(int,stdin.readline().split()))
    nums=list(map(int,stdin.readline().split()))
    for _ in range(Q):
        L,R=list(map(int,stdin.readline().split())) 
        X=L-1
        Y=R-1

        count=0

        for i in range(X,Y+1):
            for j in range(Y,X-1,-1):
                ax=nums[i]
                ay=nums[j]
                xor=ax^ay
                if ax<=xor and xor<=ay:
                    count+=1
        
        stdout.write(str(count)+'\n')
