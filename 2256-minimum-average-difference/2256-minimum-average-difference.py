class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        idx = lsum = 0
        minAvg = numsum = sum(nums) #init minAvg to some big no.
        for i in range(n):
            lsum += nums[i]
            left = lsum//(i+1)
            right = (numsum - lsum)//(n-i-1) if i!=n-1 else 0
            avgdiff = abs(left - right)
            if avgdiff < minAvg:
                minAvg = avgdiff
                idx = i
        return idx