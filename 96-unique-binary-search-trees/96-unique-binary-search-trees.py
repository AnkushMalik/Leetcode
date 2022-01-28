class Solution:
    hsh = {0:1,1:1}
    def numTrees(self, n: int) -> int:
        count = 0
        for i in range(0,n):
            if i not in self.hsh:
                self.hsh[i] = self.numTrees(i)
            if n-i-1 not in self.hsh:
                self.hsh[n-i-1] = self.numTrees(n-i-1)
            count+=self.hsh[i]*self.hsh[n-i-1]
        return count