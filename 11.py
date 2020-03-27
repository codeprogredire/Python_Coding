'''
Fast Modulo multiplication (Binary Exponentiation)
Calculating (x^n) % m
'''
# m = 10^9 + 7 
m = 1000000007


def mod_exp1(x,n):
    if n==0:
        return 1
    elif n==1:
        return x%m
    elif n%2==0:
        return mod_exp1((x%m*x%m)%m,n/2)
    else:
        return ((x%m)*(mod_exp1((x%m*x%m)%m,(n-1)/2))%m)

# Improved version (GeeksForGeeks)
def mod_exp2(x,n):
    if n==0:
       return 1
    if n==1:
        return x%m

    temp = mod_exp2(x,int(n/2))
    temp = (temp*temp)%m

    if n%2==0:
        return temp
    else:
        return ((x%m)*temp)%m

x=int(input('Enter x : '))
n=int(input('Enter n : '))
print(mod_exp1(x,n))
print(mod_exp2(x,n))
   
