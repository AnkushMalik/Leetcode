'''
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        mp = len(nums)//2
        left = self.sortArray(nums[:mp])
        right = self.sortArray(nums[mp:])
        return self.sortedMerge(left,right)
    
    def sortedMerge(self,a,b):
        if not b: return a
        if not a: return b
        
        ma = []
        
        while(len(a)!=0 and len(b)!=0):
            if(a[0]<=b[0]):
                ma.append(a.pop(0))
            else:
                ma.append(b.pop(0))
        if len(a)==0:
            ma+=b
        else:
            ma+=a
        return ma
