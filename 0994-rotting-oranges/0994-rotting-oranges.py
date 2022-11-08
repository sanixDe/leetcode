class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = []
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        fresh = 0
        
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
                    
        ans = 0
        direction = [(0,1), (0,-1),(1,0),(-1,0)]
        
                         
                                 
        while queue and fresh > 0:
            
            l = len(queue)
            print(queue)
            for i in range(l):
                i, j = queue.pop(0)
                
                for r, c in direction:
                    row = i+r
                    col = j+c
                    print(row, col)
                    if row == rows or row < 0 or col == cols or col < 0 or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    queue.append((row, col))
                    fresh -= 1
            ans += 1
                
                

        return ans if fresh == 0 else -1
            
                    
                    
        