test = int(input())

def solution(queue):
    i = 0
    n = len(queue)

    while i<n:
        if queue[i] == 0:
            i+=1
        else:
            j = i+1
            i+=1
            dist = 1
            if j<n and i<n :
                while j < n and i<n and queue[j] != 1:
                    dist += 1
                    j += 1
                    i+=1
                if dist < 6 and j!=n:
                    return False    
                elif dist<6 and j==n:
                    return True
    return True


while test:
    n = int(input())
    queue = list(map(int,input().split()))
    
    if not solution(queue):
        print('NO')    
    else:
        print('YES')

    test -= 1