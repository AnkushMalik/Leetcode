class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lattices = set()
        circles = set([tuple(c) for c in circles])
        for circle in circles:
            x,y,r = circle
            for X in range(x-r,x+r+1):
                for Y in range(y-r, y+r+1):
                    if (X-x)**2 + (Y-y)**2 - r*r<=0:
                        lattices.add((X,Y))
        return len(lattices)
            