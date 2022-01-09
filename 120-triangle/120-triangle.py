class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        self.findMinPath(triangle,0,0,memo)
        return memo[(0,0)]
    
    def findMinPath(self,triangle,i,j,memo):
        if i>=len(triangle) or j<0 or j>=len(triangle[i]): return 0
        if (i,j) in memo: return memo[(i,j)]
        memo[(i,j)] = triangle[i][j] + min(self.findMinPath(triangle,i+1,j,memo),self.findMinPath(triangle,i+1,j+1,memo))
        return memo[(i,j)]
        