'''
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''


import heapq

def findCheapestPrice(n,flights,src,dst,K):
    adj={u:[] for u in range(n)}
    
    for f in flights:
        adj[f[0]].append((f[1],f[2]))


    for u,v in adj.items():
        print('{} :'.format(u),end=' ')
        for i in v:
            print(i,end=' ')
        print()
        
    Q=[(0,src,K+1)]
    
    while len(Q):
        print('Q: {}'.format(Q))
        top=heapq.heappop(Q)
        print('top: {}'.format(top))
        d,u,e=top
        
        if u==dst:
            return d
        if e>0:
            for v in adj[u]:
                heapq.heappush(Q,(d+v[1],v[0],e-1))
                
                
    return -1
    
n=3
flights=[[0,1,100],[1,2,100],[0,2,500]]
k=1
src=0
dst=2

print(findCheapestPrice(n,flights,src,dst,k))