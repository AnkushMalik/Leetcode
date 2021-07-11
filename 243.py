'''
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        kStack = []
        def findKSmallest(node,kStack):
            if not node:
                return kStack
            if len(kStack)==0:
                kStack.append(node.val)
            else:
                if kStack[-1]>node.val:
                    for i in range(k):
                        if kStack[i]>node.val:
                            kStack = kStack[:i]+[node.val]+kStack[i:]
                            break
                else:
                    kStack.append(node.val)
            if node.left: 
                kStack = findKSmallest(node.left,kStack)
            if node.right: 
                kStack = findKSmallest(node.right,kStack)
            return kStack
        kStack = findKSmallest(root,kStack)
        return kStack[k-1]
