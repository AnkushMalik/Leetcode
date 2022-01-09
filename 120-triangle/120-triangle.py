class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def findMinPath(i,j):
            if i>=len(triangle) or j<0 or j>=len(triangle[i]): return 0
            if (i,j) in memo: return memo[(i,j)]
            memo[(i,j)] = triangle[i][j] + min(findMinPath(i+1,j),findMinPath(i+1,j+1))
            return memo[(i,j)]
        
        return findMinPath(0,0)
    
    
        