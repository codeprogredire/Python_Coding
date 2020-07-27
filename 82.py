'''
Powerset of a set. Plus, finding the largest subset in which every pair of elements is divisible by one or other.
'''

def powerset(s):
    n=len(s)
    p=pow(2,n)

    sub=[]

    for i in range(p):
        x=bin(i)[2:]
        x='0'*max(0,n-len(x))+x

        x=x[::-1]

        temp=[]

        for j,k in enumerate(x):
            if k is '1':
                temp.append(s[j])
            
        sub.append(temp)
    
    return sub

s=list(map(int,input().split()))
a=powerset(s)
a.sort(reverse=True,key=lambda x: len(x))
print(a)


for x in a:
    count=1
    for i in range(1,len(x)):
        if x[i]%x[i-1]==0:
            count+=1
    
    if count==len(x):
        print(x)
        break
        




