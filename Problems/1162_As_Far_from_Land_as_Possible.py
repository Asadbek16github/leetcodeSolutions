from collections import deque

class Solution:
    def maxDistance(grid):
        N = len(grid)
        D = deque()
        
        for x in range(N):
            for y in range(N):
                if grid[x][y]:
                    D.append([x, y])


        res = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while D:
            x, y = D.popleft()
            res = grid[x][y]

            for d_x, d_y in directions:
                newX, newY = x+d_x, y+d_y

                if(min(newX, newY)>=0 and max(newX, newY)<N and grid[newX][newY]==0):
                    D.append([newX, newY])
                    grid[newX][newY] = grid[x][y]+1

        return res-1 if res>1 else -1
