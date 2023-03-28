class Solution:
            
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # create a dictionary
        n = len(isConnected)
        root = {i:i for i in range(n)}
        
        # find method
        
        def find(x):
            
            if x == root[x]:
                return x
            else:
                return find(root[x])
                
        
        def union(x, y):
            p = find(x)
            q = find(y)
            
            if p!=q:
                root[q] = p
            
        def count():
            d = {}
            print(root)
            for k,v in root.items():
                x = find(v)
                
                if x not in d:
                    d[x] = {k}
                else:
                    d[x].add(k)
            print(d) 
            return len(d)
        
    
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
                    
        return count()