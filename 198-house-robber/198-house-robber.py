class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        mem = {}
        return max(self.robIt(nums,0,mem),self.robIt(nums,1,mem))
    
    def robIt(self, arr, idx,memo):
        if idx>=len(arr): return 0
        if idx in memo:
            return memo[idx]
        memo[idx] = max(arr[idx]+self.robIt(arr,idx+2,memo),0+self.robIt(arr,idx+1,memo))
        return memo[idx]