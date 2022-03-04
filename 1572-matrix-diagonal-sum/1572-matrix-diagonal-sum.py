class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dSum = 0
        n = len(mat)
        for i in range(0,n):
            dSum += mat[i][i]+mat[i][n-1-i]
        if n%2==0: return dSum
        else:
            return dSum - mat[n//2][n//2]