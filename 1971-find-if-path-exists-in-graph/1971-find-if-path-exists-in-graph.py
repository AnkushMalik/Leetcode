class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination: return True
        adjList = {}
        for p,q in edges:
            if p not in adjList: adjList[p]=[]
            if q not in adjList: adjList[q]=[]
            adjList[p].append(q)
            adjList[q].append(p)
        
        visited = [0]*n
        stk = [source]
        
        while(stk):
            node = stk.pop()
            visited[node]=1
            for nbr in adjList[node]:
                if nbr==destination: return True
                if visited[nbr]: continue
                stk.append(nbr)
                visited[nbr]=1
        return False
            