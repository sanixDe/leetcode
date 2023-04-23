# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs_sum(node):
            if node == None:
                return 0
            return node.val + dfs_sum(node.left) + dfs_sum(node.right)
        total_sum = dfs_sum(root)
        
        
        def dfs(node):
            if node == None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.max_sum = max(self.max_sum, (total_sum - r) * r , (total_sum - l)*l)
            return node.val + l + r
        self.max_sum = 0
        dfs(root)
        return self.max_sum % (10**9 + 7)
    
# time complexity = O(N)
# space complexity = O(1)