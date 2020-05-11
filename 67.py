'''
Factors of a number in sqrt(n) time complexity
'''

import math

N=int(input('Enter n : '))

end=int(math.sqrt(N))

factors=[]

for i in range(1,end+1):
    if N%i==0:
        factors.append(i)