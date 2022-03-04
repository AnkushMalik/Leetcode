class Solution:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        if coords[1][0]==coords[0][0]:
            slope = math.inf
        else:
            slope = (coords[1][1]-coords[0][1])/(coords[1][0]-coords[0][0])
        for i in range(1,len(coords)):
            if coords[i][0]==coords[i-1][0]:
                chk=math.inf
            else: chk = (coords[i][1]-coords[i-1][1])/(coords[i][0]-coords[i-1][0])
            if chk!=slope: return False
        return True