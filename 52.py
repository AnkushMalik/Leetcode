'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        results = []
        self.findPlacements(0,n,results,[])
        return len(results)
    def findPlacements(self,row,dim,results,colPlacement):
        if(row==dim):
            results.append(colPlacement)
        else:
            for i in range(dim):
                colPlacement.append(i)
                if self.isValidPlacement(colPlacement):
                    self.findPlacements(row+1,dim,results,colPlacement)
                colPlacement.pop()

    def isValidPlacement(self, colPlacement):
        latest_row = len(colPlacement)-1
        for i in range(latest_row):
            diff = abs(colPlacement[latest_row]-colPlacement[i])
            if diff==0 or diff == latest_row-i:
                return False
        return True
        
