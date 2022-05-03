class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]

        for i,j in walls:
            grid[i][j]='W'
        for i,j in guards:
            grid[i][j]='G'

        for i,j in guards:
            li,ri=i-1,i+1
            lj,rj=j-1,j+1
            while(li>=0 and grid[li][j]!='W' and grid[li][j]!='G'):
                grid[li][j]='X'
                li-=1
            while(ri<m and grid[ri][j]!='W' and grid[ri][j]!='G'):
                grid[ri][j]='X'
                ri+=1
            while(lj>=0 and grid[i][lj]!='W' and grid[i][lj]!='G'):
                grid[i][lj]='X'
                lj-=1
            while(rj<n and grid[i][rj]!='W' and grid[i][rj]!='G'):
                grid[i][rj]='X'
                rj+=1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0: count+=1
        return count