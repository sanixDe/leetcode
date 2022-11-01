class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        adj = {i:[] for i in range(n)}
        
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            
            
        def dfs(node):
            
            if node in visited:
                return
            
            visited.add(node)
            
            for c in adj[node]:
                dfs(c)
                
                
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
                
        return res
    
    
    '''
    Time complexity = O(n+v)

    
    '''