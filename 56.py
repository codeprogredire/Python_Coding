'''
Link : https://www.hackerrank.com/contests/hack-the-interview-ii-global/challenges/distribution-in-m-bins
'''

def maxScore(a, m):
    # Write your code here
    MOD=10**9+7
    a.sort()
    n=len(a)
    k=n//m
    r=n%m
    if r!=0:
        k-=1
        r+=m
    
    i,j=1,0
    
    score=0
    while i<=k:
        score=(score+(i*(sum(a[j:j+m])%MOD))%MOD)%MOD
        i+=1
        j+=m
    if r!=0:
        score=(score+(i*(sum(a[j:])%MOD))%MOD)%MOD
    
    return score

a=[4,1,7,9]
m=4
print(maxScore(a,m))