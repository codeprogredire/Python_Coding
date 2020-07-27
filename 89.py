'''
Link: https://www.codechef.com/COOK120B/problems/BOJACK
'''


from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    d=int(stdin.readline())
    ans='a'*d+'b'*d+'\n'
    stdout.write(str(2*d)+'\n')
    stdout.write(ans)