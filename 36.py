'''
Link : https://www.codechef.com/LRNDSA01/problems/LAPIN
'''
from math import ceil
test=int(input())

while test:
    s=input()
    n=len(s)
    str1,str2=list(s[:n//2]),list(s[ceil(n/2):])
    str1.sort()
    str2.sort()
    if str1==str2:
        print('YES')
    else:
        print('NO')
    
    test-=1