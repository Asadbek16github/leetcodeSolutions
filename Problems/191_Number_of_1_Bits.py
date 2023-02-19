# solution 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n = n >> 1
        return res
    

# solution 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    


