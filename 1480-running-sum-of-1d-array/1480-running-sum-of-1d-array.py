class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            t = nums[i]
            nums[i]+=sum
            sum+=t
        return nums