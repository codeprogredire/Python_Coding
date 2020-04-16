test=int(input())
while test:
    n=int(input())

    def perfect_power(n):
        if n==1:
            return True
        else:
            i=2
            factors={}

            while n!=1:
                if n%i==0:
                    if i in factors.keys():
                        factors[i]+=1
                    else:
                        factors[i]=1
                    n//=i
                else:
                    i+=1
            
            powers=set(factors.values())
            count=len(powers)
            return count==1 and 1 not in powers
            

    def calculate(n):
        total=0
        for i in range(1,n+1):
            if n%i==0 and perfect_power(i):
                total+=i
        return total

    ans=0
    for i in range(1,n+1):
        ans+=calculate(i)
    
    print(ans)
    test-=1


