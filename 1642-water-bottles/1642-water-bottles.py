class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res =numBottles + (numBottles - 1)//(numExchange - 1)
        return res