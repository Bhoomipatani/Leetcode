from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board[0]), len(board)
        
        def dfs(i, j, k):
            # Base cases
            if k == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[k]:
                return False
            
            # Mark the cell as visited by modifying its value temporarily
            temp, board[i][j] = board[i][j], "#"
            
            # Explore all possible directions
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))
            
            # Restore the cell's original value
            board[i][j] = temp
            
            return found
        
        # Check every cell as a starting point
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
