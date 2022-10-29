# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lower, upper):
            
            if root == None:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            

            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)

        
        return dfs(root, float('-inf'), float('+inf'))
    
    '''
    Time Complexity = O(N)
    Space Complexity = O(N) since we are using recursion so it's for recursion stack
    
    '''
                    