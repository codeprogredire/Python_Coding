'''
Link : https://www.codechef.com/COOK117B/problems/MATBREAK
'''


from sys import stdin,stdout

for i in range(int(stdin.readline())):
    n,a=[int(i) for i in stdin.readline().split()]

    ans=0
    ptot=a
    MOD=1000000007
    for i in range(n):
        pi=pow(ptot,2*i+1,MOD)
        ans=(ans+pi)%MOD
        ptot=(ptot*pi)%MOD

    stdout.write(str(ans)+'\n')

    
