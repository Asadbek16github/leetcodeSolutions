# This Breadth first search algorithm
from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        D = deque()
        ROW, COLUMN = len(mat), len(mat[0])

        for r in range(ROW):
            for c in range(COLUMN):
                if(mat[r][c]==0):
                    D.append([r, c])
                else:
                    mat[r][c]=-1
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while D:
            r, c = D.popleft()

            for d_r, d_c in directions:
                newR, newC = r+d_r, c+d_c
                if( 0<=newR<ROW  and  0<=newC<COLUMN  and  mat[newR][newC]==-1):
                    D.append([newR, newC])
                    mat[newR][newC] = mat[r][c]+1

        return mat
    





# The secon way is DP
import math
class Solution2:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        ROW, COLUMN = len(mat), len(mat[0])

        for r in range(ROW):
            for c in range(COLUMN):
                if mat[r][c]:
                    value_top = mat[r-1][c] if r else math.inf
                    value_left = mat[r][c-1] if c else math.inf

                    mat[r][c] = min(value_top, value_left) + 1
                
        for r in range(ROW-1, -1, -1):
            for c in range(COLUMN-1, -1, -1):
                if mat[r][c]:
                    value_right = mat[r][c+1] if c != COLUMN-1 else math.inf
                    value_bottom = mat[r+1][c] if r != ROW-1 else math.inf

                    mat[r][c] = min(mat[r][c], value_bottom+1, value_right+1)

        return mat
