class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                part=""
                while stack and stack[-1]!="[":
                    part=stack.pop() + part
                if stack :
                    stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                if k == "":
                    k = "1"
                stack.append(int(k) * part)
               
        return "".join(stack)

        