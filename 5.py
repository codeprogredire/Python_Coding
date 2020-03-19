'''
Finding substrings of a given string
'''

string=input('Enter the string : ')
n=len(string)

substrings=[]

for i in range(n):
    for j in range(1,n+1):
        if i+j>n:
            break
        substrings.append(string[i:i+j])

print(substrings)