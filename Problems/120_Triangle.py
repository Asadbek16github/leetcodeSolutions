
# solution 1
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)+1
        res = [0 for i in range(n)]

        for row in triangle[::-1]:
            for i in range(len(row)):
                res[i] = row[i]+min(res[i], res[i+1])

        return res[0]


# Solution 2
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if(len(triangle)==1): return triangle[0][0]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
                print()

        return triangle[0][0]