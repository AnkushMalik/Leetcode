# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if candidate==i:continue
            if knows(candidate,i):
                candidate = i
        if self.isCelebrity(candidate, n):
            return candidate
        return -1
        
    def isCelebrity(self, i, n):
        for j in range(n):
            if j==i: continue
            if knows(i,j) or not knows(j,i): return False
        return True