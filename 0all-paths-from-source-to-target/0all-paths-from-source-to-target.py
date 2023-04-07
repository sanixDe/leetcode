class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, path, paths):
            
            if node == len(graph) - 1:
                paths.append(path)
                return
            
            for n in graph[node]:
                # path.append(n)
                dfs(n, path+[n], paths)
            
        paths = []
        path = [0]
        dfs(0, path, paths)
        
        return paths
    