class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = {}
        for i in range(len(nums)):
            hsh[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hsh and hsh[comp]!=i:
                return [i,hsh[comp]]
