class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        n = len(graph)
        
        def dfs(node):
            res.append(node)
            
            if node == n-1:
                ans.append(res.copy())
                return 
            
            for i in graph[node]:
                dfs(i)
                res.pop()
            
        res = []
        dfs(0)
        return ans