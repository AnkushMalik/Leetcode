class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.findAllCombination([], k, n)
        return self.ans
    
    def findAllCombination(self, path, k, n):
        if k==0 and sum(path)==n: self.ans.append(path)
        else:
            start = path[-1]+1 if path else 1
            pathSum = sum(path)
            for i in range(start,10):
                if pathSum+i <= n:
                    self.findAllCombination(path+[i], k-1, n)
            