class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        temp=sorted(nums)
        for i in nums:
            ans.append(temp.index(i))
        return ans