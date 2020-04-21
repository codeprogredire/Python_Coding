'''
Leetcode weekly Contest 184
Link : https://leetcode.com/contest/weekly-contest-184/problems/string-matching-in-an-array/
'''
def stringMatching(words):
    if len(words)==1:
        return
    else:
        temp=[]
        ans=[]
        for i in range(len(words)):
            temp=words[:i]+words[i+1:]
            for string in temp:
                if words[i] in string:
                    ans.append(words[i])
                    break
        
        return ans

words=['hero','as','superhero','mass']
print(stringMatching(words))
        