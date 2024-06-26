class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        str1=sorted(s)
        str2=sorted(t)
        for i in range(len(s)):
            if str1[i]!=str2[i]:
                return False
        return True
        
        