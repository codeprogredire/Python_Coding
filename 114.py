from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    A=list(map(int,stdin.readline().split()))

    tot=0

    for i in range(n):
        for j in range(i+1,n):
            bij=A[i]&A[j]
            if bij==A[i]:
                tot+=1
    
    stdout.write(str(tot)+'\n')