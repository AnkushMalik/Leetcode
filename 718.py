'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

'''

#DP 2D array:
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(len(nums1)-1,-1,-1):
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i]==nums2[j]:
                    memo[i][j]=1+memo[i+1][j+1]
        return max([max(row) for row in memo])

#Hashmap: TLE
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        hsh = {}
        def findLCS(nums1,nums2,i,j,count):
            if j==len(nums2) or i==len(nums1): return count
            if (i,j,count) in hsh: return hsh[(i,j,count)]
            same = count
            if nums1[i]==nums2[j]:
                same = findLCS(nums1,nums2,i+1,j+1,count+1)
            hsh[(i,j,count)] = max(same,findLCS(nums1,nums2,i,j+1,0),findLCS(nums1,nums2,i+1,j,0))
            return hsh[(i,j,count)]
        return findLCS(nums1,nums2,0,0,0)
