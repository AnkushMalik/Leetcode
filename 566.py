'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = [ [0]*c for _ in range(r) ]
        row = 0
        col = 0
        
        if(r*c!=len(mat)*len(mat[0])):
            return mat
        
        for i in mat:
            for j in i:
                ans[row][col]=j
                col+=1
                if(col>=c):
                    col=0
                    row+=1
        if row!=r or col!=0:
            return mat
        return ans
