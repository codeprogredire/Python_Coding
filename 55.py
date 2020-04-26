from sys import stdin,stdout

test=int(stdin.readline())

for i in range(1,test+1):
    n,a,b,c,d=[int(i) for i in stdin.readline().split()]
    min_grain=(a-b)*n
    max_grain=(a+b)*n
    min_pack=(c-d)
    max_pack=(c+d)
    
    if max_grain<min_pack or min_grain>max_pack:
        stdout.write('No\n')
    else:
        stdout.write('Yes\n')
    