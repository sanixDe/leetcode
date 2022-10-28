# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        res = []
        if root == None:
            return res
        while queue:
            cur, level = queue.pop()
            if len(res) == level:
                res.append([])
            
            res[level].append(cur.val)
            
            if cur.right:
                queue.append((cur.right, level+1))
            if cur.left:
                queue.append((cur.left, level+1))
            
        return res