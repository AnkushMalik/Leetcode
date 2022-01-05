class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        ans = [ [R+C] * C for _ in range(R)]
        
        for i in range(R):
            for j in range(C):
                if mat[i][j]==0:
                    ans[i][j]=0
                else:
                    if i>0:
                        ans[i][j] = min(ans[i][j],ans[i-1][j]+1)
                    if j>0:
                        ans[i][j] = min(ans[i][j],ans[i][j-1]+1)
        for i in range(R-1,-1,-1):
            for j in range(C-1,-1,-1):
                if i<R-1:
                    ans[i][j] = min(ans[i][j],ans[i+1][j]+1)
                if j<C-1:
                    ans[i][j] = min(ans[i][j],ans[i][j+1]+1) 
        return ans