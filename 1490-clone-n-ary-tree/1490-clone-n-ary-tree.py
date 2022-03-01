class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None
        def dfs(orig):
            cnode = Node(orig.val,[])
            cnode.children = [dfs(i) for i in orig.children]
            return cnode
        return dfs(root)