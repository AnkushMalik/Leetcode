'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        if len(nums)==1: return TreeNode(nums[0])
        
        n = len(nums)//2
        
        lTree = nums[:n]
        rTree = nums[n+1:]
        root = TreeNode(nums[n])
        root.left = self.sortedArrayToBST(lTree)
        root.right = self.sortedArrayToBST(rTree)
        
        return root
