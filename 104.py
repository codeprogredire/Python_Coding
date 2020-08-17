'''
Link: http://codeforces.com/contest/1399/problem/B
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    candies=list(map(int,stdin.readline().split()))
    oranges=list(map(int,stdin.readline().split()))

    mo=min(oranges)
    mc=min(candies)

    count=0

    for i in range(n):
        count+=max(candies[i]-mc,oranges[i]-mo)
    
    stdout.write(str(count)+'\n')

