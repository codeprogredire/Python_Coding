'''
Mo's algorithm
Sum of every query range
'''

from sys import stdin,stdout
import math

n=int(stdin.readline())
arr=list(map(int,stdin.readline().split()))

q=int(stdin.readline())
queries=[]

for i in range(q):
	query=list(map(int,stdin.readline().split()))
	query+=[i]
	queries.append(query)

queries.sort()
queries.sort(key=lambda x:x[1])


ml=0;mr=-1;currSum=0

ans=[]

for query in queries:
	L=query[0]
	R=query[1]

	while ml<L:
		currSum-=arr[ml]
		ml+=1

	while ml>L:
		ml-=1
		currSum+=arr[ml]

	while mr<R:
		mr+=1
		currSum+=arr[mr]

	while mr>R:
		currSum-=arr[mr]
		mr-=1

	temp=[currSum,query[2]]
	ans.append(temp)

ans.sort(key=lambda x:x[1])

for a in ans:
	print(a[0])
