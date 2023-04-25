class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        queue = [(sr,sc)]
        # node = queue.pop()
        # print(queue.pop())
        
        n = len(image)
        m = len(image[0])
        
        given_color = image[sr][sc]
        
        if color == given_color:
            return image
        
        while queue:
            x, y = queue.pop()
            
            # if node not in seen:
            #     x, y = node
            image[x][y] = color
            if x-1 >= 0 and image[x-1][y] == given_color:
                image[x-1][y] = color
                queue.append((x-1,y))
            if y-1 >= 0 and image[x][y-1] == given_color:
                image[x][y-1] = color
                
                queue.append((x,y-1))
            if x+1 < n and image[x+1][y] == given_color:
                image[x+1][y] = color
                
                queue.append((x+1,y))
            if y+1 < m and image[x][y+1] == given_color:
                image[x][y+1] = color
                
                queue.append((x,y+1))
                    
        return image
                
        