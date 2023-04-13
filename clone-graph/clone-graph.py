"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def dfs(node):
            if node == None:
                return None
            
            if node in visited:
                return visited[node]
            
            copy_node = Node(node.val, [])
            
            visited[node] = copy_node
            
        
        
            if node.neighbors != None:
                for i in node.neighbors:
                    print("neighbor",node.val,i.val)
                    copy_node.neighbors.append(dfs(i))
                
            return copy_node
        return dfs(node)