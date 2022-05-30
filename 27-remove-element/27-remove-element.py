class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        c = 0
        while(i<=j):
            if nums[j]==val:
                j-=1
                c+=1
            else:
                if nums[i]==val:
                    c+=1
                    nums[i],nums[j]=nums[j],nums[i]
                    j-=1
                i+=1
        return len(nums)-c