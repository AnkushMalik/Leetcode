class Solution:
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
ans = [ [0] * len(mat[0]) for _ in range(len(mat))]
for i in range(len(mat)-1,-1,-1):
for j in range(len(mat[i])-1,-1,-1):
if mat[i][j]!=0:
ans[i][j] = min(self.calcDist(mat,i-1,j,1,{}),self.calcDist(mat,i,j-1,1,{}))
return ans
def calcDist(self, mat, i, j, dist, hsh):
if 0<i or j<0:
return len(mat)+len(mat[0])
if (i,j) in hsh: return hsh[(i,j)]
if(mat[i][j]==0):
hsh[(i,j)]=0
if (i,j) in hsh: return
R = len(mat)
C = len(mat[0])
hsh[(i,j)] = t = d = l = r = R+C
if 0<i:
t = self.calcDist(mat, i-1, j, dist, hsh)
if i<R-1:
d = self.calcDist(mat, i+1, j, dist, hsh)
if 0<j:
l = self.calcDist(mat, i, j-1, dist, hsh)
if j<C-1:
r = self.calcDist(mat, i, j+1, dist, hsh)
hsh[(i,j)] = dist + min(t,d,l,r)
return hsh[(i,j)]