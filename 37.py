'''
Link : https://www.codechef.com/LRNDSA01/problems/ZCO14003
'''

n=int(input())
budgets=[0]*n

for i in range(n):
    budgets[i]=int(input())

budgets.sort()

revenue=float('-inf')

for i,budget in enumerate(budgets):
    revenue=max(revenue,budget*(n-i))

print(revenue)