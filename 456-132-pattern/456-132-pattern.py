class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        currMin = nums[0]
        stk = [] #()
        for i in range(1, len(nums)):
            while stk and nums[i]>=stk[-1][0]: stk.pop()
            if stk and stk[-1][1]<nums[i]: 
                return True
            stk.append((nums[i], currMin))
            currMin = min(currMin,nums[i])
        return False