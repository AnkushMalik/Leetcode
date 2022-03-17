class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def tracking(arr,path,i):
            if i==len(graph)-1:
                ans.append(path[:])
            else:
                for e in arr:
                    tracking(graph[e], path+[e], e)
        tracking(graph[0], [0], 0)
        return ans