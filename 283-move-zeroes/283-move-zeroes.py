class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNZ = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[lastNZ]=nums[i]
                lastNZ+=1
        for i in range(lastNZ,len(nums)): nums[i]=0