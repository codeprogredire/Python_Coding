from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n,k=list(map(int,stdin.readline().split()))
    steps=list(map(int,stdin.readline().split()))

    ans=''

    for step in steps:
        if step%k==0:
            ans+='1'
        else:
            ans+='0'

    stdout.write(str(ans)+'\n')

