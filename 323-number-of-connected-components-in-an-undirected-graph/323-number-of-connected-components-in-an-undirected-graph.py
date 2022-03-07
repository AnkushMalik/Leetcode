class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        
        for p,c in edges:
            adjList[p].append(c)
            adjList[c].append(p)
        
        count = 0
        visited = [0]*n
        for i in range(n):
            if visited[i]==0:
                count+=1
                stk = [i]
                visited[i]=1
                while(stk):
                    node = stk.pop()
                    for nbr in adjList[node]:
                        if visited[nbr]==0:
                            visited[nbr]=1
                            stk.append(nbr)
        return count
            