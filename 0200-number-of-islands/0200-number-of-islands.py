class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, i, j):
            
            if grid[i][j] == '1':
                grid[i][j] = "-1"
                
            if i > 0 and grid[i-1][j] == '1':
                dfs(grid, i-1, j)
            if i < len(grid)-1 and grid[i+1][j] == '1':
                dfs(grid,i+1,j)
            if j > 0 and grid[i][j-1] == '1':
                dfs(grid, i, j-1)
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                dfs(grid, i, j+1)
                 
            
            
            
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, i, j)
                    
        return count