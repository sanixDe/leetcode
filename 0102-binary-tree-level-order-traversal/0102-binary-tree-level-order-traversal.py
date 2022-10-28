# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue = [(root, 0)]
        
#         res = []
        
#         while queue:
#             cur, level = queue.pop(0)
            
#             if level == len(res):
#                 res.append([])
            
#             res[level].append(cur.val)
            
#             if cur.left:
#                 queue.append((cur.left, level+1))
#             if cur.right:
#                 queue.append((cur.right, level+1))
#         return res

        if root == None:
            return []
        queue = [root]
        
        res = []
        while queue:
            
            levels = []
            
            cur_len = len(queue)
            
            for i in range(cur_len):
                node = queue.pop(0)
                
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            
            res.append(levels)
            
        
        return res