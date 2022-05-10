class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.findAllCombination([], k, n)
        return self.ans
    
    def findAllCombination(self, path, k, n):
        if len(path)==k:
            if sum(path)==n: self.ans.append(path)
        else:
            start = path[-1]+1 if path else 1
            for i in range(start,10):
                if sum(path)+i <= n:
                    self.findAllCombination(path+[i], k, n)
            