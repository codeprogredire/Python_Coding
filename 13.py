'''
nth fibonacci number
0,1,1,2,3,..
'''

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a


n = int(input('Enter n : '))

print('{}'.format(fibonacci(n)))
