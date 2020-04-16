test = int(input())

while test:
    n = int(input())
    cars = list(map(int,input().split()))

    cars.sort(reverse=True)

    profit = 0

    mod = 1000000007
    for i in range(n):
        profit = profit + max(cars[i]-i,0)

    
    print(profit%mod)

    test -= 1