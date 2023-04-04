class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adjecency list
        graph = {i:[] for i in range(n)}
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        
        visited = set()
        def dfs(n, pre):
            
            if n in visited:
                return False
            visited.add(n)
            
            for i in graph[n]:
                if i == pre:
                    continue
                if i in visited:
                    return False
                dfs(i, n)
            return True
        return dfs(0, -1) and len(visited)==n
        
        