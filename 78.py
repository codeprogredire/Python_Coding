from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    N=int(stdin.readline())
    coins=list(map(int,stdin.readline().split()))

    ans='YES\n'
    
    tens=0
    fives=0
    
    for coin in coins:
        if coin==5:
            fives+=1
        else:
            if coin==10:
                if fives:
                    fives-=1
                else:
                    ans='NO\n'
                    break
            elif coin==15:
                if tens:
                    tens-=1
                elif fives>=2:
                    fives-=2
                else:
                    ans='NO\n'
                    break

        


    stdout.write(ans)            
