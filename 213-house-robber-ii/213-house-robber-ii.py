class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        resA = self.robIt(nums[:len(nums)-1], 0, {})
        resB = self.robIt(nums[1:], 0, {})
        return max(resA,resB)
    
    def robIt(self, arr, idx,memo):
        if idx>=len(arr): return 0
        if idx in memo:
            return memo[idx]
        memo[idx] = max(arr[idx]+self.robIt(arr,idx+2,memo),self.robIt(arr,idx+1,memo))
        return memo[idx]