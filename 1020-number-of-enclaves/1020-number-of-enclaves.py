class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j, count):
            if (i == -1 or j == -1 or i == n or j == m or grid[i][j] == 0):
                # if :
                #     return 0
                return 0
                
#             if :
#                 return
            
            grid[i][j] = 0 
            count += 1
            count += dfs(i-1, j, count)
            count += dfs(i+1, j, count)
            count += dfs(i, j+1, count)
            count += dfs(i, j-1, count)
            return count
            
        
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1):
                    if grid[i][j] == 1:
                        # print(i, j)
                        count += dfs(i, j, 0)
        
        # print(grid, count)
        return(sum(sum(grid, [])))
        return 0