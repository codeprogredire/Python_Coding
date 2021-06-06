'''
Link: https://cses.fi/problemset/task/1069
'''

from sys import stdin,stdout

string = stdin.readline().rstrip('\n')
n = len(string)

char = string[0]
length = 1
ans = 1

for i in range(1,n):
    if string[i] == char:
        length += 1
    else:
        char = string[i]
        ans = max(ans,length)
        length = 1

ans = max(ans,length)

stdout.write(str(ans))