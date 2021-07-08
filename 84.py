'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.findLargestArea(heights)
    
    def findLargestArea(self, heights):
        if len(heights)==0:
            return 0
        if len(heights)==1:
            return heights[0]
        if len(heights)==2:
            return min(heights)*2 if min(heights)!=0 else max(heights)
        if(min(heights)==max(heights)): return len(heights)*min(heights)

        minVal = min(heights)
        min_pt = heights.index(minVal)
        
        return max(
            len(heights)*minVal,
            self.findLargestArea(heights[0:min_pt]),
            self.findLargestArea(heights[min_pt+1:len(heights)])
        )
