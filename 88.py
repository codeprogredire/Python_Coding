from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    nums=list(map(int,stdin.readline().split()))

    temp=0

    hashmap={}

    nums.sort(reverse=True)

    ans='YES\n'

    for x in nums:
        temp|=x
        if temp in hashmap:
            ans='NO\n'
            break
        else:
            hashmap[temp]=1

    stdout.write(ans)
    

