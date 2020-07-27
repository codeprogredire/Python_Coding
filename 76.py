from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    N,K=list(map(int,stdin.readline().split()))
    prices=list(map(int,stdin.readline().split()))
    loss=0

    for price in prices:
        if price>K:
            loss+=(price-K)
    
    stdout.write(str(loss)+'\n')