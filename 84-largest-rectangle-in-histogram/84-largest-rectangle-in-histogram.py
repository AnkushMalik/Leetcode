class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def findMaxArea(heights):
            if not heights: return 0
            if len(heights)==1: return heights[0]
            minVal = min(heights)
            if(minVal==max(heights)): return len(heights)*minVal
            minPt = heights.index(minVal)
            
            return max(
                minVal*len(heights),
                findMaxArea(heights[:minPt]),
                findMaxArea(heights[minPt+1:])
            )
        return findMaxArea(heights)