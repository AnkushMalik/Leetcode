class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        t = 0
        iFlag = 0
        fFlag = 0
        for i in range(len(nums)):
            if nums[i]!=sortedNums[i]:
                if t == 0:
                    iFlag = i
                else:
                    fFlag = i
                t=1
        return fFlag-iFlag+1 if fFlag else 0