'''
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

 

Example 1:


Input: preorder = [5,2,1,3,6]
Output: true
Example 2:

Input: preorder = [5,2,6,1,3]
Output: false
'''
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower = -1
        stk = []
        for elem in preorder:
            if elem<lower: return False
            while stk and elem>stk[-1]:
                lower = stk.pop()
            stk.append(elem)
        return True
