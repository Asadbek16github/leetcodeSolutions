# The first solution
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        ROW, COLUMN = len(mat), len(mat[0])

        if(ROW*COLUMN != r*c): return mat

        output = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for dr in range(ROW):
            for dc in range(COLUMN):
                output[k//c][k%c] = mat[dr][dc]
                k+=1
        return output
    

# the second soution
class Solution2     :
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        ROW, COLUMN = len(mat), len(mat[0])
        d = []

        if(ROW*COLUMN == r*c):
            for dr in range(ROW):
                for dc in range(COLUMN):
                    d.append(mat[dr][dc])

            d = d[::-1]
            res = []
            for d_r in range(r):
                res1 = []
                for d_c in range(c):
                    res1.append(d.pop())
                res.append(res1)
            
            return res
        else:
            return mat