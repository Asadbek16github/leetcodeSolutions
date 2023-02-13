class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row, column = len(grid), len(grid[0])
        visited = set()

        def DFS(r, c):
            if( r<0 or r==row or c<0 or c==column or grid[r][c]==0 or (r, c) in visited): return 0

            visited.add((r, c))
            return 1 + DFS(r+1, c)+DFS(r-1, c)+DFS(r, c+1)+DFS(r, c-1)

        res = 0
        for r in range(row):
            for c in range(column):
                res = max(res, DFS(r, c))

        return res