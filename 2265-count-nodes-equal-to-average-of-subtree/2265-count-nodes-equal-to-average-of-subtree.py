class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        allSubtrees, count = [], 0
        def dfs(node):
            subtree = [node.val] # root of subtree will be first element
            if node.left:  subtree+=dfs(node.left)
            if node.right:  subtree+=dfs(node.right)
            allSubtrees.append(subtree) # register subtree
            return subtree
        dfs(root)

        for subtree in allSubtrees:
			# if avg of subtree == subtree[0] (root) then count++
            if sum(subtree)//len(subtree) == subtree[0]: count+=1
        return count