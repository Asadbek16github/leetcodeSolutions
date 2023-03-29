class Solutions:
    def MinimumPathSum(self, grid):

        row, column = len(grid), len(grid[0])
        for i in range(row):
            grid[i].append(float('inf'))

        grid = grid + [[float('inf') for i in range(column+1)]]
        grid[row][column-1]=0


        for r in range(row-1, -1, -1):
            for c in range(column-1, -1, -1):
                grid[r][c] = grid[r][c] + min(grid[r+1][c], grid[r][c+1])

        return grid[0][0]

print(Solutions().MinimumPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))