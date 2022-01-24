class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>=0:
                if currsum<0:
                    currsum=nums[i]
                else:
                    currsum+=nums[i]
            else:
                if currsum+nums[i]>=0:
                    currsum+=nums[i]
                else:
                    currsum=nums[i]
            maxsum = max(maxsum,currsum)
        return maxsum