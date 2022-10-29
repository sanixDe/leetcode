# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        def helper(l, r):
            nonlocal position
            if l > r:
                return None
            
            root_val = preorder[position]
            root = TreeNode(root_val)
            
            position += 1
            
            root.left = helper(l, dict[root_val] - 1)
            root.right = helper(dict[root_val] + 1, r)
            
            return root
        
        
        position = 0
        dict = {}
        
        for i in range(len(inorder)):
            dict[inorder[i]] = i
        return helper(0, len(preorder)-1)
        
        '''
        Time complexity = O(N)
        Space Complexity = O(N) Hashmap and system stack used by recursion calls
        
        '''