class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj = {i:[] for i in range(n)}

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        # ans = False
        
        
        visited = set()
        def dfs(node):
            visited.add(node)
            print(node)
            if node == destination:
                print(node, destination)
  
                return True
            
            for i in adj[node]:
                if i not in visited:
                    if dfs(i) == True:
                        return True
                    
                else:
                    continue
            
            return False
        
        return dfs(source)