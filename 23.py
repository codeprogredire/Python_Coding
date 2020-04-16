a=[10,6,4,1,2]

a.sort(reverse=True)

profit = 0
n=len(a)
for i in range(n):
    profit += max(a[i]-i,0)

print(profit)