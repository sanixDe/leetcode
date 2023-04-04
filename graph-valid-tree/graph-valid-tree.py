class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Steps
        # First make the adjacency list
        # Then apply DFS 
        # if the visiting node is already visited then there is loop and return false
        
        # making a adjacency list
        adj = {i:[] for i in range(n)}
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        visited = set()

        # dfs
        def dfs(i, pre):
            if i in visited:
                return False
            visited.add(i)
            
            for j in adj[i]:
                if j == pre:
                    continue
                if j in visited:
                    return False
                dfs(j, i)
            
            return True
        return dfs(0, -1) and n == len(visited)