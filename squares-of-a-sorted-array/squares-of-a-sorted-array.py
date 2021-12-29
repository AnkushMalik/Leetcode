class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stk = []
        i = 0
        j = len(nums)-1
        while i < j:
            sql = nums[i]**2
            sqr = nums[j]**2
            if(sql<=sqr):
                stk.insert(0,sqr)
                j-=1
            else:
                stk.insert(0,sql)
                i+=1
        stk.insert(0,nums[i]**2)
        return stk