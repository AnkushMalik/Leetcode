'''
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
'''

class Solution:
	def partitionDisjoint(self, nums: List[int]) -> int:
		n = len(nums)
		maxRange = [None]*n
		minRange = [None]*n
	
		m = nums[0]
		for i in range(n):
			m = max(m,nums[i])
			maxRange[i]=m
		
		m = nums[-1]
		for i in range(n-1,-1,-1):
			m = min(nums[i],m)
			minRange[i]=m
		
		for i in range(1,n):
			if maxRange[i-1]<=minRange[i]:
				return i

#better:
'''
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = nums[0]
        curMax = nums[0]
        ans = 1
        for i, num in enumerate(nums):
			# If current number is smaller than left maximum, the answer is no longer valid.
			# Now the current index is the last index of left and the maximum is now left maximum.
            if num < leftMax:
                ans = i+1  
                leftMax = curMax
			# Update the current maximum
            curMax = max(curMax, num)

        return ans
'''