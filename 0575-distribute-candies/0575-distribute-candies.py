class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count=Counter(candyType)
        n=len(candyType)
        if n//2<=len(count):
            return n//2
        else:
            return len(count)
        