class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def dfs(i, j):
            
#             # count += grid[i][j]
#             print(i, j, grid[i][j])
#             grid[i][j] = -1
#             # count += 1
#             if i+1<n and grid[i+1][j] == 1:
#                 count += 1+dfs(i+1, j, count)
#             if i-1>=0 and grid[i-1][j] == 1:
#                 count += 1+dfs(i-1, j, count)
#             if j+1<m and grid[i][j+1] == 1:
#                 count += 1+dfs(i, j+1, count)
#             if j-1>=0 and grid[i][j-1] == 1:
#                 count += 1+dfs(i, j-1, count)
#             print(count)
#             print(grid)
#             return count
            
            if not (i >= 0  and i < n and j >= 0 and j < m and (i, j) not in seen and grid[i][j] == 1):
                return 0
            seen.add((i, j))
            return 1 + dfs(i+1,j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)
        
        
        
        n = len(grid)
        m = len(grid[0])
        max_count = 0
        for i in range(n):
            for j in range(m):
                # if grid[i][j] == 1:
                    
                max_count = max(max_count, dfs(i, j))
                    # print(max_count)
                    # print(max_count)
                    
                    
        return max_count