class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for i in range(9):
            check_r = set()
            check_c = set()
            for j in range(9):
                if(board[i][j] != '.'):
                    if(board[i][j] not in check_r):
                        check_r.add(board[i][j])
                    else:
                        return False
                
                if(board[j][i] != '.'):
                    if(board[j][i] not in check_c):
                        check_c.add(board[j][i])
                    else:
                        return False
        
        q, p = 3, 3
        q_prev, p_prev = 0, 0
        while q<=9 and p<=9:
            check = set()
            for i in range(q_prev, q):
                for j in range(p_prev, p):
                    if(board[i][j] != '.'):
                        if(board[i][j] not in check):
                            check.add(board[i][j])
                        else:
                            return False

            if(q!=9 and p!=9):
                p_prev = p
                p+=3
            elif(q!=9 and p==9):
                p_prev = 0
                q_prev = q
                q+=3
                p=3
            elif(q==9 and p!=9):
                p_prev = p
                p+=3
            else:
                break
        
        return True