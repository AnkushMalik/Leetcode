class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = {}
        for p,q in edges:
            if p not in adjList: adjList[p]=[]
            if q not in adjList: adjList[q]=[]
            adjList[p].append(q)
            adjList[q].append(p)
        
        visited = [0]*n        
        def dfs(node):
            if node == destination: return True
            for nbr in adjList[node]:
                if visited[nbr]: continue
                visited[nbr]=1
                if dfs(nbr): return True
            return False
                
        return dfs(source)
            