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
                
                