'''
Fast modulo multiplication
'''

from sys import stdin,stdout

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


stdout.write(str(fexp(5,100000)))