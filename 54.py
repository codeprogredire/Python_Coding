'''
Link : https://www.codechef.com/problems/CKISSHUG
'''

from sys import stdin,stdout

test=int(stdin.readline())

MOD=10**9+7

def fexp(base,exp):
    if exp==0:
        return 1
    if exp==1:
        return base%MOD
    temp=fexp(base,exp//2)%MOD
    if exp%2==0:
        return (temp*temp)%MOD
    else:
        return (base*temp*temp)%MOD


for _ in range(test):
    n=int(stdin.readline())

    if n%2:
        exp=(n+1)//2+1
        ans=fexp(2,exp)-2
    else:
        exp=n//2
        ans=(fexp(2,exp)+fexp(2,exp+1)-2)%MOD
    stdout.write(str(ans)+'\n')
    