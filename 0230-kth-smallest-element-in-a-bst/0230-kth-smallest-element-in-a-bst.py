# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root, res):
            if root == None:
                return True
            
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
            return res
        
        res = []
        return(inorder(root, res)[k-1])