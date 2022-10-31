class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Adjecency list
        adj = {i:[] for i in range(n)}
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        print(adj)
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            
            for x in adj[node]:
                dfs(x)
        
    

            
        ans = 0
        for i in range(n):
            if i not in visited:
                print(i)
                dfs(i)
                ans += 1
        
        return ans
        
