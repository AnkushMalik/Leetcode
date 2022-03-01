class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root: ans = Node(root.val,[])
        else: return None
        def dfs(node,orig):
            if not orig: return
            for i in orig.children:
                node.children.append(Node(i.val,[]))
                dfs(node.children[-1],i)
        dfs(ans,root)
        return ans