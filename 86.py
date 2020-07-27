from sys import stdin,stdout

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None




for _ in range(int(stdin.readline())):
    N,Q=list(map(int,stdin.readline().split()))
    values=list(map(int,stdin.readline().split()))
    edges=[]

    for _ in range(N-1):
        edge=tuple(map(int,stdin.readline().split()))
        edge=(edge[0]-1,edge[1]-1)
        edges.append(edge)

    print(edges)
    
