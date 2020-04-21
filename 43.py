

from sys import stdin,stdout

test=int(stdin.readline())

for _ in range(test):
    k,d0,d1=[int(i) for i in stdin.readline().split()]
    
    s=(d0+d1)
    c=((2*s)%10)+((4*s)%10)+((8*s)%10)+((6*s)%10)

    num_of_cycles=(k-3)//4

    tot=0
    if k==2:
        tot=s
    else:
        tot=s+(s%10)+c*num_of_cycles
        left_over=(k-3)-(num_of_cycles*4)

        p=2
        for _ in range(left_over):
            tot+=((p*s)%10)
            p*=2

    if tot%3:
        stdout.write('NO')
    else:
        stdout.write('YES')
    stdout.write('\n')