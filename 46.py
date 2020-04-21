def fib(k):
    a=1
    b=1
    seq=[1,1]
    while True:
        a,b=b,a+b
        if b>k:
            break
        else:
            seq.append(b)

    return seq


seq=fib(k)
count=0
j=len(seq)-1

while k>0:
    count+= k//seq[j]
    k=k%seq[j]
    j-=1

print(count)

