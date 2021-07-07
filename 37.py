'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
'''

class Solution:
    solvedSudoku = None
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.sudokuSolver(board,0,0)
        for i in range(9):
            for j in range(9):
                board[i][j]=self.solvedSudoku[i][j]
            

    def sudokuSolver(self, board, row, col):
        if row==9:
            self.solvedSudoku=[x[:] for x in board]
        else:
            if board[row][col]!='.':
                if col==8:
                    self.sudokuSolver(board,row+1,0)
                else:
                    self.sudokuSolver(board,row,col+1)
            else:
                for n in range(1,10):
                    if(self.isValid(board,row,col,n)):
                        board[row][col]=str(n)
                        if col==8:
                            self.sudokuSolver(board,row+1,0)
                        else:
                            self.sudokuSolver(board,row,col+1)
                        board[row][col]="."

    def isValid(self, board, i, j, n):
        if str(n) in board[i]:
            return False
        cols = [k[j] for k in board]
        if str(n) in cols:
            return False

        row_min = 3*(i//3)
        row_max = row_min+3
        col_min = 3*(j//3)
        col_max = col_min+3
        for row in range(row_min,row_max):
            for col in range(col_min,col_max):
                if board[row][col]==str(n):
                    return False
        return True
