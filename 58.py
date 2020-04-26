from sys import stdin,stdout


test=int(stdin.readline())
for _ in range(test):
    n,s=[int(i) for i in stdin.readline().split()]
    prices=[int(i) for i in stdin.readline().split()]
    tag=[int(i) for i in stdin.readline().split()]
    
    d=float('inf')
    f=float('inf')

    for i,p in enumerate(tag):
        if p==0:
            if prices[i]<d:
                d=prices[i]
        else:
            if prices[i]<f:
                f=prices[i]
    
    bal=100-s
    if (d+f)>bal:
        stdout.write('no\n')
    else:
        stdout.write('yes\n')


