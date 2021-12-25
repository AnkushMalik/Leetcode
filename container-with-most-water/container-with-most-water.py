class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i = 0
        j = len(height)-1
        while(i<j):
            currarea = min(height[i],height[j])*(j-i)
            maxarea = max(maxarea, currarea)
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return maxarea
                