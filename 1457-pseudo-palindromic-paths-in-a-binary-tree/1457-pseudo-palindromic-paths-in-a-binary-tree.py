class Solution:
    def __init__(self):
        self.d = {}
        self.ans = 0
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if root.val in self.d:
            self.d[root.val] += 1
        else:
            self.d[root.val] = 1
        
        if root.left:
            self.pseudoPalindromicPaths(root.left) 
        if root.right:
            self.pseudoPalindromicPaths(root.right)
        
        if not root.left and not root.right:
            count = 0
            for x in self.d:
                if self.d[x]%2 == 1:
                    count += 1
            if count <= 1:
                self.ans += 1
        self.d[root.val] -= 1
        return self.ans