import numpy as np

test = int(input())

while test:
    n = int(input())
    nums = list(map(int,input().split()))

    seqs=[]
    for i in range(1,n+1):
        for j in range(n):
            if i+j<=n:
                seqs.append(nums[j:i+j])    

    count=0
    for seq in seqs:
        seq=np.array(seq)
        if np.prod(seq)%4!=2:
            count+=1
    
    print(count)
    test-=1