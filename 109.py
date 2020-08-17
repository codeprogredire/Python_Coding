from sys import stdin,stdout

n=int(stdin.readline())

strings=[]
for _ in range(n):
    temp=stdin.readline().rstrip('\n')
    strings.append(temp)

p=stdin.readline().rstrip('\n')

np=len(p)

ans=[]
for s in strings:
    ns=len(s)
    for i in range(ns-np+1):
        for j in range(np):
            if s[i+j]!=p[j]:
                break
        if j==np-1:
            ans.append(s)

print(ans)




