class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = (high-low)//2
        
        if(low%2==0 and high%2==0):
            return res
        else:
            return res+1