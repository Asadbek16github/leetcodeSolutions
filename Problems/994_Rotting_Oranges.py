# the first solution

from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        D = deque()
        counter = 0
        lr, lc = len(grid), len(grid[0])
        for r in range(lr):
            for c in range(lc):
                if(grid[r][c]==2):
                    D.append([r,c])
                elif(grid[r][c]==1):
                    counter+=1
                else:
                    continue
        if not D and not counter:
            return 0
        elif( not D and counter):
            return -1
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        min = 0
        q = len(D)
        t = 0
        while D:
            r, c = D.popleft()
            t+=1


            for d_r, d_c in directions:
                new_r, new_c = r+d_r, c+d_c
                if(0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and grid[new_r][new_c]==1):
                    counter-=1
                    D.append([new_r, new_c])
                    grid[new_r][new_c]=2
            
            if(t==q):
                min+=1
                q = len(D)
                t = 0

        return -1 if counter else min-1
    


# the second solution

class Solution2:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        D = deque()
        ROW, COLUMN = len(grid), len(grid[0])
        time, fresh = 0, 0

        for r in range(ROW):
            for c in range(COLUMN):
                if(grid[r][c]==2):
                    D.append([r,c])
                elif(grid[r][c]==1):
                    fresh+=1

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while D and fresh:
            
            x = len(D)
            for i in range(x):
                r,c = D.popleft()

                for dr, dc in directions:
                    newR, newC = r+dr, c+dc
                    if(0<=newR<len(grid) and 0<=newC<len(grid[0]) and grid[newR][newC]==1):
                        fresh-=1
                        grid[newR][newC]=2
                        D.append([newR, newC])

            time+=1
        return -1 if fresh else time