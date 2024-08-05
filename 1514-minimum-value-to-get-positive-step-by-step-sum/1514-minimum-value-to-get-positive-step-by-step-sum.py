class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=0
        mini=1
        for i in nums:
            prefix=prefix+i
            mini=max(mini,1-prefix)
        return mini