class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        result=[]
        def getcol(row,board):
            for col in range(n):
                if board[row][col]=='Q':
                    return col

        def isvalid(row,col,board):
            for i in range(row):
                j = getcol(i,board)
                if i+j == row+col:
                    return False
                if i-j == row-col:
                    return False
                if j==col:
                    return False
            return True

        def backtracking(row,col,board):
            board[row][col]='Q'
            if isvalid(row,col,board) :
                if row==n-1:
                    result.append([''.join(row) for row in board])
                else:
                    for j in range(n):
                        backtracking(row+1,j,board)
            board[row][col]='.'
            

        for i in range(n):
            backtracking(0,i,board)

        return result
        