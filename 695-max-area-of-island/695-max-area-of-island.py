class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxarea = 0
        for row in range(len(grid)):
            for col in  range(len(grid[row])):
                if grid[row][col]==1:
                    self.maxarea = max(self.floodFill(grid,row,col,0),self.maxarea)
        return self.maxarea

    def floodFill(self, grid, i, j, area):
        grid[i][j]='X'
        area+=1
        if i>0 and grid[i-1][j]==1:
            area=self.floodFill(grid,i-1,j,area)
        if j>0 and grid[i][j-1]==1:
            area=self.floodFill(grid,i,j-1,area)
        if i<len(grid)-1 and grid[i+1][j]==1:
            area=self.floodFill(grid,i+1,j,area)
        if j<len(grid[0])-1 and grid[i][j+1]==1:
            area=self.floodFill(grid,i,j+1,area)
        return area
            