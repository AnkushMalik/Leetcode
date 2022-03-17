class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        group = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        def find(x):
            if x!=group[x]:
                x = find(group[x])
            return group[x]
        
        def union(ga,gb):
            if ga==gb: return
            if rank[ga]>rank[gb]:
                group[gb]=ga
            else:
                group[ga]=gb
                if rank[ga]==rank[gb]:
                    rank[gb]+=1
        
        for p,q in edges:
            gp = find(p)
            gq = find(q)
            if gp!=gq:
                union(gp,gq)
        
        return find(source)==find(destination)
            