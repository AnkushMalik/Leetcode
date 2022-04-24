class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lattices = set()
        tcircles = set()
        for c in circles:
            tcircles.add(tuple(c))
        for circle in tcircles:
            x,y,r = circle
            for X in range(x-r,x+r+1):
                for Y in range(y-r, y+r+1):
                    if (X-x)**2 + (Y-y)**2 - r*r<=0:
                        lattices.add((X,Y))
        return len(lattices)
            