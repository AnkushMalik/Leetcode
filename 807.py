'''
You are given an n x n integer matrix grid where grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

In the end, the skyline when viewed from all four directions of the grid (i.e., top, bottom, left, and right) must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance.

Return the maximum total sum that the height of the buildings can be increased.

Note that all buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
'''

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        tdv = []
        lrv = []
        for i in grid:
            lrv.append(max(i))

        tv = list(map(list, zip(*grid)))
        for i in tv:
            tdv.append(max(i))
        sum = 0
        for i in range(len(tdv)):
            for j in range(len(lrv)):
                initial_h = grid[i][j]
                new_height = min(tdv[i],lrv[j])
                grid[i][j] = new_height
                sum+= new_height-initial_h
        return sum