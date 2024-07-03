class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=0
        curr=0
        for i in range(len(gain)):
            curr=curr+gain[i]
            maxi=max(maxi,curr)
        return maxi
        
        