# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_val = p.val
        q_val = q.val
        
        root_val = root.val
        
        if root_val > p_val and root_val > q_val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root_val < p_val and root_val < q_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

''' 
Time Complexity = O(N) worst case vising all the nodes

Space Complexity = O(N) using recursion stack


'''