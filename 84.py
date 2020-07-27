from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    nums=list(map(int,stdin.readline().split()))

    ans='YES\n'
    for num in nums:
        if num%2==0:
            ans='NO\n'
            break

    stdout.write(ans)
    
