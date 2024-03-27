class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board = ['.'*n for _ in range(n)]

        def issafe(row,col):
            duprow = row
            dupcol = col
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            col = dupcol
            row = duprow
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1

            row = duprow
            col = dupcol
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1


            return True
            
        def nqueens(col):
            if col==n:
                ans.append(board[:])
                return
            for row in range(n):
                if issafe(row,col):
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                    nqueens(col+1)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]
        
        nqueens(0)
        return ans