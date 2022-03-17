class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        group = [i for i in range(n)]
        def find(x):
            if x!=group[x]:
                x = find(group[x])
            return group[x]
        
        def union(ga,gb):
            if ga==gb: return
            group[ga]=gb
        
        for p,q in edges:
            gp = find(p)
            gq = find(q)
            if gp!=gq:
                union(gp,gq)
        
        return find(source)==find(destination)
            