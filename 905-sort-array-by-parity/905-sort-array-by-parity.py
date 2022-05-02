class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j = 0, len(nums)-1
        while(i<j):
            if nums[i]%2==0:
                i+=1
            else:
                if nums[j]%2==0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j-=1
                    continue
            if nums[j]%2:
                j-=1
                
        return nums