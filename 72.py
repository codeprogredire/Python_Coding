'''
Link: https://codeforces.com/contest/144/problem/A
'''


from sys import stdin,stdout

n=int(stdin.readline())

heights=list(map(int,stdin.readline().split()))

mini=float('inf')
maxi=float('-inf')
min_index=0
max_index=0

for i,v in enumerate(heights):
    if mini>=v:
        mini_index=i
        mini=v
    if maxi<v:
        maxi_index=i
        maxi=v


if mini_index>maxi_index:
    ans=(n-1-mini_index)+maxi_index
else:
    ans=(n-1-mini_index)+(maxi_index-1)

stdout.write(str(ans))