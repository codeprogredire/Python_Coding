'''
Link : https://www.codechef.com/LRNDSA01/problems/LADDU
'''

from sys import stdin,stdout

test=int(stdin.readline())

for _ in range(test):
    activities,origin=stdin.readline().split()
    laddus=0
    for _ in range(int(activities)):
        activity=stdin.readline().split()

        if activity[0]=='CONTEST_WON':
            laddus+=300+max(0,20-int(activity[1]))
        elif activity[0]=='TOP_CONTRIBUTOR':
            laddus+=300
        elif activity[0]=='BUG_FOUND':
            laddus+=int(activity[1])
        else:
            laddus+=50 # activity=='CONTEST_HOSTED'
    
    if origin=='INDIAN':
        stdout.write(str(laddus//200))
    else:
        stdout.write(str(laddus//400))
    stdout.write('\n')
