class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        
        for x, y in connections:
            adj[x].append(y)
            adj[y].append(x)
            
        
        seen = set()
        
        
        def dfs(node):
            
            if node in seen:
                return
            
            seen.add(node)
            
            for new_node in adj[node]:
                
                dfs(new_node)
            
            return
    
    
        ans = 0
        network = 0
        if len(connections) < n - 1:
            return -1
        
        for i in range(n):
            if i not in seen:
                network += 1
                dfs(i)
        return network - 1 
                
            
            
        