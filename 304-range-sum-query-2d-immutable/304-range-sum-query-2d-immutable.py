class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        for i in range(0, row):
            rowval = 0
            for j in range(col):
                dp[i][j] = matrix[i][j] + rowval
                if i>0: dp[i][j]+=dp[i-1][j]
                rowval+=matrix[i][j]
        print(dp)
        self.dp = dp
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp
        ans = dp[row2][col2]
        if row1>0:
            ans-=dp[row1-1][col2]
        if col1>0:
            ans-=dp[row2][col1-1]
        if row1>0 and col1>0:
            ans+=dp[row1-1][col1-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)