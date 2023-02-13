from collections import deque
class Solution:
    def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        prev = image[sr][sc]
        Dec = deque()
        hset = set()

        Dec.append([sr, sc])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while Dec:
            r, c = Dec.popleft()
            image[r][c]=color
            hset.add((r,c))

            for d_r, d_c in directions:
                newR, newC = r+d_r, c+d_c

                if((newR, newC) not in hset and 0<=newR<len(image) and 0<=newC<len(image[0]) and image[newR][newC]==prev):
                    Dec.append([newR, newC])

        return image
    
print(Solution.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))

