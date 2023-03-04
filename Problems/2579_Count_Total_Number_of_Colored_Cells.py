class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1: return 1


        oddSum = 0
        oddNum = 1
        
        for i in range(n-1):
            oddSum+=oddNum
            oddNum+=2

        return oddSum*2 + oddNum
            