class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                return self.findChunk(nums, mid, target)
        return [-1,-1]
    def findChunk(self, arr, i, target):
        j = i
        while(i>=0 or j<len(arr)):
            if(i>-1 and arr[i]==target):
                i-=1
            elif(j<len(arr) and arr[j]==target):
                j+=1
            else:
                break
        return [i+1,j-1]