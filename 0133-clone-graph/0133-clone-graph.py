"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dict = {}
        
        def dfs(node):
            
            if node in dict:
                return dict[node]
            
            if node == None:
                return None
            
            copy = Node(node.val)
            dict[node] = copy
            
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
                
            return copy
        
        return dfs(node)
    
    '''
    Time complexity : O(N x M) N as in nodes and M as in edges
    Space complexity : O(N) N as in number of Nodes
    
    '''