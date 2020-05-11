'''
Greatest Common Divisor(GCD) of two numbers
'''

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)


print(gcd(8,12))
print(gcd(3,17))