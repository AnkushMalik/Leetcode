class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        uniq = []
        self.findAllCombs(candidates,target,[])
        for i in self.ans:
            if i not in uniq: uniq.append(i)
        return uniq
    
    def findAllCombs(self,arr,t,path):
        if t==0:
            self.ans.append(sorted(path[:]))
        if t<0:
            return
        for i in arr:
            path.append(i)
            self.findAllCombs(arr,t-i,path)
            path.pop()