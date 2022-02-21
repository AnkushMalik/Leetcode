class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hsh = {}
        for i in nums:
            if i in hsh: 
                hsh[i]+=1
                if hsh[i]>len(nums)//2: return i
            else: hsh[i]=1
        return nums[0]