from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    x,y=list(map(int,stdin.readline().split()))
    a,b=list(map(int,stdin.readline().split()))

    if x==0 or y==0:
        if x==0:
            ans=a*y
        else:
            ans=b*y
    else:
        mini=min(x,y)
        maxi=max(x,y)

        if 2*a < b:
            ans=(x+y)*a
        else:
            ans=b*mini + a*(maxi-mini)
        
    stdout.write(str(ans)+'\n')
