'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        a = len(nums)-1
        count = 0
        while(a>1):
            b = 0
            c = a-1
            while(c>b):
                if nums[b]+nums[c]>nums[a]:
                    count+=c-b
                    c-=1
                else:
                    b+=1
            a-=1
        return count
