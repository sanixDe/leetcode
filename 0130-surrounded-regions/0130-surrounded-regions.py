class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(i,j):
            
            board[i][j] = -1
            
            if i > 0 and board[i-1][j] == 'O':
                dfs(i-1,j)
            if i < len(board)-1 and board[i+1][j] == 'O':
                dfs(i+1,j)
            if j > 0 and board[i][j-1] == 'O':
                dfs(i,j-1)
            if j < len(board[0]) -1  and board[i][j+1] == 'O':
                dfs(i,j+1)
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                    if board[i][j] == 'O':
                        
                        dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == -1:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'