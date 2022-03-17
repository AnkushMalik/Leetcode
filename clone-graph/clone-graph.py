"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        hsh = {}
        def cloner(node):
            if node.val in hsh: return hsh[node.val]
            cnode = Node(node.val,[])
            hsh[node.val]=cnode
            for nbr in node.neighbors:
                if nbr.val not in hsh:
                    hsh[nbr.val] = cloner(nbr)
                cnode.neighbors.append(hsh[nbr.val])
            return cnode
        return cloner(node)
        
        