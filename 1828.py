'''
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.


'''

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            i_p = 0
            for p in points:
                condn = (q[0]-p[0])**2+(q[1]-p[1])**2-q[2]**2
                if(condn<=0):
                    i_p+=1
            ans.append(i_p)
        return ans
