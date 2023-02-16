class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROW, COLUMN = len(matrix), len(matrix[0])

        start_R, stop_R = 0, ROW-1

        while stop_R>start_R:
            mid = (start_R+stop_R)//2
            if(matrix[mid][0]==target):
                return True
            elif(matrix[mid][0]>target):
                stop_R = mid-1
            elif(matrix[mid][0]<target and matrix[mid][COLUMN-1]>target):
                start_R = mid
                break
            elif(matrix[mid][COLUMN-1]==target):
                return True
            else:
                start_R = mid+1 

        
        return True if target in matrix[start_R] else False