test = int(input())

while test:
    n = input()
    reversedNo = n[::-1]
    print(reversedNo.lstrip('0'))
    test -= 1
