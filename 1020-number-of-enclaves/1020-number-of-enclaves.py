class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            if i < 0 or j < 0 or i > n-1 or j > m-1 or grid[i][j] == 0:
                return
            grid[i][j] = 0
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    if grid[i][j] == 1:
                        dfs(i, j)
        print(grid)
        return sum(sum(grid, []))