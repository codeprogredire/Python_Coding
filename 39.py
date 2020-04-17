'''
Link : https://www.codechef.com/LRNDSA01/submit/CARVANS
'''


from sys import stdin,stdout

test=int(stdin.readline())

while test:
    n=int(stdin.readline())
    cars=list(map(int,stdin.readline().split()))

    count=1

    for i in range(1,n):
        if cars[i]<=cars[i-1]:
            count+=1
        else:
            cars[i]=cars[i-1]
    
    stdout.write(str(count))
    stdout.write(str('\n'))
    test-=1
