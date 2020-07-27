'''
Link:https://www.codechef.com/COOK120B/problems/EVENTUAL
'''

from sys import stdin,stdout
from collections import Counter

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    s=stdin.readline().rstrip('\n')
    counter=Counter(s)
    values=list(counter.values())

    ans='YES\n'
    for v in values:
        if v%2!=0:
            ans='NO\n'
            break

    stdout.write(ans)

