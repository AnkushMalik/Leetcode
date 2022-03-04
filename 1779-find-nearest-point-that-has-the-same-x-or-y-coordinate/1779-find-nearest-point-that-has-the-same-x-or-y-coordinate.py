class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minPt = []
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                hDist = abs(points[i][0]-x)+abs(points[i][1]-y)
                if not minPt or hDist<minPt[0]:
                    minPt=[hDist,i]
        return minPt[1] if minPt else -1