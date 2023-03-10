class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]

        for i in range(2, numRows+1):
            res = []
            prev = 0
            prevList = ans[-1]
            for j in range(i//2):
                val = prevList[j]+prev
                res.append(val)
                prev = prevList[j]

            if i%2 == 0:
                res = res[:] + res[::-1]

            else:
                res = res[:] + [prev + prevList[i//2]] + res[::-1]

            ans.append(res)
        return ans

print(Solution().generate(5))