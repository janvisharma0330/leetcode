class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        seen={}
        for i in nums2:
            while (stack and i > stack[-1]):
                c=stack.pop()
                seen[c]=i
            stack.append(i)
        return [seen.get(i,-1) for i in nums1]        