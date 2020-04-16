prices = list(map(int,input().split()))

n = len(prices)

buy=0
profit=0

if n==1:
    profit=0
else:
    for i in range(1,n):
        if prices[i-1]<prices[i] and buy==0:
            buy=prices[i-1]
            print(buy)
        if prices[i-1]>prices[i] and buy!=0:
            profit+=prices[i]-buy
            buy=0
        if i==n-1 and buy!=0:
            print(i)
            profit+=prices[i]-buy

print(profit)
