from sys import stdin,stdout

s=stdin.readline().rstrip('\n')
n=len(s)
t=stdin.readline().rstrip('\n')
q=int(stdin.readline())

for _ in range(q):
    row=int(stdin.readline())

    string=''
    for i in range(row):
        string+=s[i%n]
    
    ans=string.count(t)

    stdout.write(str(ans)+'\n')
