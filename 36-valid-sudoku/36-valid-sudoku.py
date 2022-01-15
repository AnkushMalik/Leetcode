class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check1 = self.subBoxChecker(board)
        if not check1: return check1
        check2 = self.checkRowCol(board)
        return check2
    
    def checkRowCol(self,board):
        for i in range(9):
            for j in range(9):
                chk = board[i][j]
                if chk.isdigit():
                    col = [row[j] for row in board[i+1:]]
                    if chk in board[i][j+1:] or chk in col: return False
        return True
                    
                    
                    
    
    def subBoxChecker(self,board):
        chkpoints = [3,6,9]
        for i in chkpoints:
            for j in chkpoints:
                start = i-3
                end = j-3
                chk = [0]*10
                for k in range(i-3,i):
                    for l in range(j-3,j):
                        if board[k][l].isdigit():
                            chk[int(board[k][l])]+=1
                            if chk[int(board[k][l])]==2:
                                return False
        return True