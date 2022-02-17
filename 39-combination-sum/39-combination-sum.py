class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.findAllCombs(candidates,target,[])
        return self.ans
    
    def findAllCombs(self,arr,t,path):
        if t==0:
            combo = sorted(path)
            if combo not in self.ans: self.ans.append(combo)
        if t<0: return
        for i in arr:
            self.findAllCombs(arr,t-i,path+[i])