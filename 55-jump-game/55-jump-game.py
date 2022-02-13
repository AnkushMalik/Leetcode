class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ptr = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]==0:
                continue
            elif(nums[i]>=len(nums)-1-i):
                ptr = i
            else:
                if nums[i]>=(ptr-i):
                    ptr = i
        return ptr==0