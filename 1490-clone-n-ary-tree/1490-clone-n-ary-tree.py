class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None
        cnode = Node(root.val,[])
        cnode.children = [self.cloneTree(i) for i in root.children]
        return cnode