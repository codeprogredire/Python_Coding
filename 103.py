'''
Link: http://codeforces.com/contest/1399/problem/A
'''

from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    nums=list(map(int,stdin.readline().split()))

    nums.sort()

    ans='YES\n'

    for i in range(n-1):
        if nums[i+1]-nums[i]>1:
            ans='NO\n'
            break

    stdout.write(ans)