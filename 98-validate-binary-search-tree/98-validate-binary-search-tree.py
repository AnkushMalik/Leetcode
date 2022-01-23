class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        def checkChildVals(root,target,checkSmall):
            if not root:
                return True
            if checkSmall:
                if root.val>=target:
                    return False
            else:
                if root.val<=target:
                    return False
            return checkChildVals(root.left,target,checkSmall)*checkChildVals(root.right,target,checkSmall)
        
        isBST = checkChildVals(root.left,root.val,True)
        if not isBST: return False
        isBST*=checkChildVals(root.right,root.val,False)
        if not isBST: return False
        return isBST*self.isValidBST(root.left)*self.isValidBST(root.right)