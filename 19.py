'''
Happy number -- Leetcode
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by 
the sum of the squares of its digits, and repeat the process 
until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
'''

def isHappy(n):
    sums=[n]
    while True:
        n=str(n)
        val=0
        for i in n:
            val=val+int(i)**2

        if val==1:
            return True
        elif val in sums:
            return False
        else:
            sums.append(val)
            n=val

print(isHappy(19))
print(isHappy(3))
print(isHappy(5))
print(isHappy(11))
print(isHappy(9))





