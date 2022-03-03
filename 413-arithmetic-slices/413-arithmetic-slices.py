class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        self.ans = 0
        self.countSlices(nums)
        return self.ans
    
    def countSlices(self, nums):
        for i in range(len(nums)-2):
            size = 3
            diff = nums[i+1]-nums[i]
            if nums[i+2]-nums[i+1]==diff:
                self.ans+=1
                for j in range(i+3,len(nums)):
                    if nums[j]-nums[j-1]==diff:
                        self.ans+=1
                    else: break