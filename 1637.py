'''
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
'''

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xcoords = sorted(list(map(list,zip(*points)))[0]) #transpose and feed points in list and select first item(xcoordinates)
        max_area = 0
        top = xcoords.pop()
        while(len(xcoords)!=0):
            newtop = xcoords.pop()
            diff = top-newtop
            if max_area<diff:
                max_area=diff
            if(max_area>=newtop):
                return max_area
            top = newtop
        return max_area