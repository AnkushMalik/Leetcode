class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        adjList = [[] for _ in range(n)]
        for A,B in edges:
            adjList[A].append(B)
            adjList[B].append(A)

        parent = {0:-1}
        stack = [0]
        
        while stack:
            node = stack.pop()
            for children in adjList[node]:
                if children == parent[node]:
                    continue
                if children in parent:
                    return False
                parent[children]=node
                stack.append(children)
        return len(parent)==n