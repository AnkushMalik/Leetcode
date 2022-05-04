class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        i,j = 0, len(nums)-1
        count = 0
        while(i<j):
            sm = arr[i]+arr[j]
            if sm==k:
                i+=1
                j-=1
                count+=1
            elif sm<k:
                i+=1
            else:
                j-=1
        return count