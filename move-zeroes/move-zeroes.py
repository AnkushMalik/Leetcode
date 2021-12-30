class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1
        i = 0
        while(i<len(nums)):
            if zero==-1:
                if nums[i]==0:
                    zero = i
            else:
                if nums[i]!=0:
                    nums[zero] = nums[i]
                    nums[i]=0
                    i = zero-1
                    zero = -1
            i+=1
        return nums