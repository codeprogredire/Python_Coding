'''
Link : https://www.codechef.com/MAY20B/problems/CORUS
'''


from sys import stdin,stdout
from collections import defaultdict

for _ in range(int(stdin.readline())):
    N,Q=list(map(int,stdin.readline().split()))
    s=str(stdin.readline().rstrip('\n'))

    freq=defaultdict()
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1

    count=[]
    for i,v in freq.items():
        if v!=1:
            count.append(v)



    for i in range(Q):
        C=int(stdin.readline())
        if C==0:
            ans=N
        elif len(count)==0:
            ans=0
        else:
            ans=0
            for item in count:
                item-=C
                if item>0:
                    ans+=item
        stdout.write(str(ans)+'\n')



    
