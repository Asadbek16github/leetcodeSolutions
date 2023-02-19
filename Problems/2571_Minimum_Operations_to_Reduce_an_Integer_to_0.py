class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n:
            if n % 2 == 0:
                n >>= 1
            elif ( n & 2 ) >0:
                res += 1
                n += 1
            else:
                res+=1
                n >>= 2

        return res
