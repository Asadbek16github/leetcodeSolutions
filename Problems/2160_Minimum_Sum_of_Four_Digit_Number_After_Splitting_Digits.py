class Solution:
    def minimumSum(self, num: int) -> int:
        res = []
        for i in range(4):
            res.append(num%10)
            num //=10
        res.sort()
        return 10*(res[0]+res[1])+(res[2]+res[3])