class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.findAllComb(1,n+1,[],k)
        return self.ans

    def findAllComb(self, start, end, carr, lim):
        if len(carr)==lim:
            self.ans.append(carr[:])
        else:
            for i in range(start,end):
                carr.append(i)
                self.findAllComb(i+1, end, carr,lim)
                carr.pop()