class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges: return source==destination
        adjList = {}
        for p,q in edges:
            if p==destination: return False
            if p not in adjList: adjList[p]=[]
            if q not in adjList: adjList[q]=[]
            adjList[p].append(q)

        def dfs(node):
            if node==destination: return True
            elif not adjList[node] or adjList[node].count('X')==len(adjList[node]): return False
            for i in range(len(adjList[node])):
                nbr = adjList[node][i]
                if nbr==node: return False
                if nbr=='X': continue
                adjList[node][i]='X'
                if not dfs(nbr): return False
                adjList[node][i]=nbr
            return True
        return dfs(source)