class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.getAllSubsets(nums,0,[])
        return self.ans
    
    def getAllSubsets(self,arr,idx,ss):
        if idx>=len(arr):
            self.ans.append(ss)
        else:
            self.getAllSubsets(arr,idx+1,ss+[arr[idx]])
            self.getAllSubsets(arr,idx+1,ss)