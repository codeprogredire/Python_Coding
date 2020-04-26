'''
Link : https://www.hackerrank.com/contests/hack-the-interview-ii-global/challenges/maximal-char-requests
'''

def getMaxCharCount(s, queries):
    # queries is a n x 2 array where queries[i][0] and queries[i][1] represents x[i] and y[i] for the ith query.
    ans=[]
    s=s.lower()
    
    for query in queries:
        start=query[0]
        end=query[1]+1
        sub=s[start:end]
        sub.sort(reverse=True)
        ans.append(sub.count(sub[0]))
    
    return ans


