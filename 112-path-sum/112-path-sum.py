class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if(not root):
            return False
        if(not root.left and not root.right):
            return True if targetSum==root.val else False
        leftSum = self.hasPathSum(root.left, targetSum-root.val) if root.left else False
        rightSum = self.hasPathSum(root.right, targetSum-root.val) if root.right else False
        
        return bool(leftSum+rightSum)