class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        
        visited = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        # print(adj)
        def dfs(k):
            visited.add(k)
            # print(k)
            for i in adj[k]:
                if i not in visited:
                    dfs(i)
        
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
                
        return count
