class Solution:
    def removeOuterParentheses(self, S):
        res, stack = [], 0
        for c in S:
            if c == '(' and stack > 0: res.append(c)
            if c == ')' and stack > 1: res.append(c)
            stack += 1 if c == '(' else -1
        return "".join(res)

        