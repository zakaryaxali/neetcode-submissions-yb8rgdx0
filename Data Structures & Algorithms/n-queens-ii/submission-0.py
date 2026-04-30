class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [0]*n 
        result = 0

        def isvalid(row,board):
            col=board[row]
            for prevrow, prevcol in enumerate(board[:row]):
                if prevrow+prevcol == row+col:
                    return False
                if prevrow-prevcol == row-col:
                    return False
                if prevcol==col:
                    return False
            return True

        def backtracking(row, board):
            nonlocal result
            if not isvalid(row,board):
                return
            if row==n-1:
                result+=1
                return
            for newcol in range(n):
                board[row+1]=newcol
                backtracking(row+1,board)


        for i in range(n):
            board[0]=i
            backtracking(0,board)

        return result

        