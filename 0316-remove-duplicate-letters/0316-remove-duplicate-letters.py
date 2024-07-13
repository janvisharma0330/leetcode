class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = [] 
        occurrence = {} 
        seen = set()
        
        for i in range(len(s)):
            occurrence[s[i]] = i
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and s[i] < stack[-1] and occurrence[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)