class Solution:
    def backspace(self,s):
        s=s.lstrip('#')
        i=0
        while i<len(s):
            if s[i]=='#':
                s=s[:max(0,i-1)]+s[i+1:]
                i-=1
                print(s)
            else:
                i+=1
        return s
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        if len(s)==1 and len(t)==1:
            return s==t
        else:
            s=self.backspace(s)
            t=self.backspace(t)
            return s==t
        
sol=Solution()
s="cv##pzk###t##m#p#qb##o##kmenj##zto###"
print(s)

print(sol.backspace(s))