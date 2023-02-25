import math
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        res = 0
        buyPrice = math.inf
        for i in prices:
            if i<buyPrice:
                buyPrice = i
            res = max(res, i-buyPrice)

        return res