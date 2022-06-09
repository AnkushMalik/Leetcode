class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rt = len(nums)-1
        while rt>0 and nums[rt]>target:
            rt-=1
        lt = 0
        while(lt<rt):
            currsum = nums[lt]+nums[rt]
            if currsum==target: return [lt+1,rt+1]
            elif currsum>target:
                rt-=1
            else:
                lt+=1
        if lt==rt: return [lt+1,rt+2]