class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1=[]
        for c in s:
            if c=="#" and len(res1)!=0 :
                res1.pop()
            elif c!="#":
                res1.append(c)
        res2=[]
        
        for c in t:
            if c=="#" and len(res2)!=0 :
                res2.pop()
            elif c!="#":
                res2.append(c)
           
        
        
        return res1==res2
