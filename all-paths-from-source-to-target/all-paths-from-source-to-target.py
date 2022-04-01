class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def tracking(arr,path,i):
            if i==len(graph)-1:
                ans.append(path[:])
            else:
                for e in arr:
                    path.append(e)
                    tracking(graph[e], path, e)
                    path.pop()
        tracking(graph[0], [0], 0)
        return ans