class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        pacs = set()
        atls = set()
        visited = set()
        def dfs(r,c,visited, preH):
            if (r,c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < preH:
                return
            
            visited.add((r,c))
            
            dfs(r-1,c,visited,heights[r][c])
            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
                
        
        for c in range(cols):
            dfs(0, c, pacs, heights[0][c])
            dfs(rows-1, c, atls, heights[rows-1][c])
            
        
        for r in range(rows):
            dfs(r, 0, pacs, heights[r][0])
            dfs(r, cols-1, atls, heights[r][cols-1])
            
            
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacs and (i,j) in atls:
                    res.append([i,j])
                    
                    
        return res
    
    '''
    Time Complexity :O(M x N) 
    Space complexity : O(M + N)
    
    '''
        