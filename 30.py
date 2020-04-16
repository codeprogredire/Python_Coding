test=int(input())

while test:
    n,k=list(map(int,input().split()))
    day,total,val=1,1,1

    while total<k:
        val*=2
        if val>n:
            val=1
            k-=total
            day+=1
            total=0
        else:
            day+=1
            total=val
    
    print(day)
    test-=1