'''
Link : https://www.codechef.com/MAY20B/problems/COVID19
'''


from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    N=int(stdin.readline())
    dist=list(map(int,stdin.readline().split()))

    i=0;m=N;M=1
    while i<N:
        j=i
        while ((j+1)<N and (dist[j+1]-dist[j])<=2):
            j+=1
        
        count=j-i+1
        if count>M:
            M=count
        if count<m:
            m=count
        i=j+1
    ans=str(m)+' '+str(M)+'\n'
    stdout.write(ans)