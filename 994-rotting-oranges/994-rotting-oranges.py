class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        rotten = []
        freshCount = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]==2:
                    rotten.append([i,j])
                elif grid[i][j]==1:
                    freshCount+=1
        count = 0
        while rotten:
            temp = []
            for org in rotten:
                i = org[0]
                j = org[1]
                if 0<i and grid[i-1][j]==1:
                    temp.append([i-1,j])
                    grid[i-1][j]=2
                    freshCount-=1
                if i<R-1 and grid[i+1][j]==1:
                    temp.append([i+1,j])
                    grid[i+1][j]=2
                    freshCount-=1
                if 0<j and grid[i][j-1]==1:
                    temp.append([i,j-1])
                    grid[i][j-1]=2
                    freshCount-=1
                if j<C-1 and grid[i][j+1]==1:
                    temp.append([i,j+1])
                    grid[i][j+1]=2
                    freshCount-=1
            rotten = temp
            if rotten:
                count+=1
        return count if not freshCount else -1